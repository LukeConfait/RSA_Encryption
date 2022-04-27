from math import log, ceil
from random import Random


def large_primes_list(lower_bound, number):
    """Produces a list with length number of primes greater than the lower bound"""

    n = lower_bound + number
    upperbound = ceil(n * (log(n) + log(log(n)) + 2))
    primes = [y for y in range(2, upperbound)]
    for prime in primes:
        num = prime
        while num < upperbound:
            num += prime
            if num in primes:
                primes.remove(num)

    large_primes = []
    for prime in primes:
        if prime >= lower_bound:
            large_primes.append(prime)

    return large_primes[0:number]


def primes_for_encryption(lower_bound, number):
    """Returns 2 random primes from within the list of primes of length number starting from the lower bound"""
    prime_list = large_primes_list(lower_bound, number)
    primes = []
    random = Random()
    primes.append(random.choice(prime_list))
    prime_list.remove(primes[0])
    primes.append(random.choice(prime_list))

    primes = random.choices(large_primes_list(lower_bound, number), k=2)
    return primes


def totient(prime1, prime2):

    """Evaluates Euler's totient function"""
    return (prime1 - 1) * (prime2 - 1)


def gcd(x, y):
    """Calculates the greatest common divisor of x and y"""

    while x != 0 and y != 0:

        if x > y:
            x %= y
        else:
            y %= x

    return max(x, y)


def public_exponent(prime1, prime2):
    """Calculates the Public exponent"""

    T = True
    e = 3

    while T == True:
        g = gcd(totient(prime1, prime2), e)
        if g == 1:
            return e
        e += 1


def private(prime1, prime2):
    """Generates the hidden part of the private key using the 2 prime numbers"""

    tot = totient(prime1, prime2)
    e = public_exponent(prime1, prime2)
    return pow(e, -1, tot)


class EncryptionKeys:
    """Generate a public and private key for encryption and decryption"""

    def __init__(self, lower_bound=500, number=10):
        self.primes = primes_for_encryption(lower_bound, number)

        self.private_key = [
            self.primes[0] * self.primes[1],
            private(self.primes[0], self.primes[1]),
        ]

        self.public_key = [
            self.primes[0] * self.primes[1],
            public_exponent(self.primes[0], self.primes[1]),
        ]

    def get_primes(self):
        return self.primes

    def get_private_key(self):
        return self.private_key

    def get_public_key(self):
        return self.public_key


def encrypt(public_key, data_to_encrypt: int):
    """Encrypt data of type int"""
    return (data_to_encrypt ** public_key[1]) % public_key[0]


def decrypt(private_key, data_to_decrypt: int):
    """Decrypt data of type int"""
    return (data_to_decrypt ** private_key[1]) % private_key[0]


keys = EncryptionKeys()

private_key = keys.get_private_key()
public_key = keys.get_public_key()

encrypted = encrypt(public_key, 91)
print(encrypted)
decrypted = decrypt(private_key, encrypted)
print(decrypted)
