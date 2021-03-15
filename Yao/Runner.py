import crypten

from Yao.Alice import Alice
from Yao.Bob import Bob


# from Yao.Participant import Participant


def main():
    crypten.init()
    alice = Alice()
    bob = Bob(alice)

    bob.send_y_enc()

    # For MPI-based implementation
    # participants = Participant()
    # participants.perform_comparison()


if __name__ == '__main__':
    main()
