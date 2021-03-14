import random

import crypten

from OT.Alice import Alice
from OT.Primes import get_random_prime_smaller, get_random_prime_small


class Bob:
    # Initialize y to be Bob's threshold, promo1/2 to be two promo codes, two random messages, and Alice the customer
    def __init__(self, y, promo0, promo1, alice: Alice):
        self.y = y
        self.promo0 = promo0
        self.promo1 = promo1
        self.e = get_random_prime_small()
        self.d = get_random_prime_smaller()
        self.N = self.e * self.d
        self.x0 = random.randint(10, 99)
        self.x1 = random.randint(10, 99)
        # self.G = next_prime(self.pubkey.n)
        self.alice = alice
        crypten.init()
        print(f"Bob: y={y}, promo0={promo0}, promo1={promo1}")

    def exec_ot(self):
        self._send_pubkey_rand()
        self._send_threshold()

    # Send Bob's public key to Alice
    def _send_pubkey_rand(self):
        self.alice.recv_pubkey_rand(self.e, self.N, self.x0, self.x1)

    # Send encrypted threshold to Alice and perform operation to obfuscate both promo code, then send it back to alice
    def _send_threshold(self):
        v = self.alice.recv_threshold(crypten.cryptensor(self.y, ptype=crypten.mpc.ptype.binary))

        k0 = (v - self.x0) ** self.d % self.N
        k1 = (v - self.x1) ** self.d % self.N

        p0 = self.promo0 + k0
        p1 = self.promo1 + k1

        self.alice.recv_promos(p0, p1)
