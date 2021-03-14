import random

import crypten
import crypten.communicator as comm
import crypten.mpc as mpc
import torch


class Participant:
    @mpc.run_multiprocess(world_size=2)
    # Encrypt the tensor and send it to the receiver
    def perform_comparison(self):
        # Generate a random number
        x_num = random.randrange(1, 100)

        # Obtain the current user's rank
        rank = comm.get().get_rank()
        print(f"Rank {rank}:\n x: {x_num}\n")

        dst = (rank + 1) % 2
        src = (rank - 1) % 2

        # Encrypt tensor
        x_tensor = torch.tensor(x_num)
        x_enc = crypten.cryptensor(x_tensor, ptype=crypten.mpc.binary, src=rank)

        # Send the result to receiver if current user is sender
        received = torch.tensor([rank])
        if rank == 0:
            comm.get().send_obj(x_tensor, dst=dst)
            print(f"{rank} sent data {x_tensor} to {dst}\n")

        comm.get().recv_obj(src=src)
        print(f"{rank} received data {received} from {src}\n")

        if rank == 1:
            result = x_enc > received
            print(f"The comparison result is {result}")
            result_tensor = torch.tensor(int(result))
            comp_result_enc = crypten.cryptensor([int(result)])
            comm.get().send_obj(result_tensor, dst=dst)
