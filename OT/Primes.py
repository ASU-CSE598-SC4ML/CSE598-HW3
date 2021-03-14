import random

primes_smaller = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]

primes_small = [23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131,
                137, 139, 149, 151]


# Return a random prime from 11 to 61
def get_random_prime_smaller():
    return random.choice(primes_smaller)


# Return a random prime from 23 to 151
def get_random_prime_small():
    return random.choice(primes_small)
