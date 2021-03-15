import crypten

from Yao.Alice import Alice


class Bob:
    # Initialize private data
    def __init__(self, alice: Alice):
        self.y = 5
        self.alice = alice
        print(f"Bob: y value is {self.y}")

    # Transmit encrypted y value to Alice
    def send_y_enc(self):
        result = self.alice.compare(crypten.cryptensor(self.y, ptype=crypten.mpc.ptype.binary))
        print("Bob: received encrypted result from Alice")
        if result.get_plain_text().item() == 1.0:
            print("Bob: x is lower or equal to y")
        else:
            print("Bob: x is greater than y")
