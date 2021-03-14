import random


class Alice:
    # Initialize x to be Alice's credit score and generate random k
    def __init__(self, x):
        self.x = x
        self.k = random.randint(10, 99)  # Toned down to the level Python can handle
        self.e = 0
        self.N = 0
        self.x0 = 0
        self.x1 = 0
        self.sel = -1
        print(f"Alice: x={x}")

    # Receive public key and random messages from Bob
    def recv_pubkey_rand(self, e, N, x0, x1):
        self.e = e
        self.N = N
        self.x0 = x0
        self.x1 = x1

    # Receive encrypted threshold from Bob and decide which promo code to obtain
    def recv_threshold(self, y_enc):
        result = y_enc >= self.x
        if result.get_plain_text().item() == 1.0:
            self.sel = 1
            x_sel = self.x1
            print("Alice: x is lower or equal to y, selecting promo1")
        else:
            self.sel = 0
            x_sel = self.x0
            print("Alice: x is greater than y, selecting promo0")

        v = (x_sel + self.k ** self.e) % self.N

        return v

    # Receive two obfuscated promo code and reveal the correct one
    def recv_promos(self, p0, p1):
        if self.sel == 0:
            promo = p0
        else:
            promo = p1
        print(f"Alice: obtained promo code {self.sel}")
