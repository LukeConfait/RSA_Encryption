
class encryption:

    def __init__(self,primes):
        self.primes = primes


    def totient(self):
        return((self.primes[0]-1)*(self.primes[1]-1))


    def gcd(x,y):

        while x != 0 and y != 0:

            if x > y:
                x %= y
            else:
                y %= x

        return max(x,y)

    def public_exponent(self):
        T = True
        e = 3

        while T == True:
            g = encryption.gcd(encryption.totient(self),e)
            if g == 1:
                break
            e += 1

        return e

    def private(self):

        totient = encryption.totient(self)
        e = encryption.public_exponent(self)

        last_rem, rem = abs(e), abs(totient)
        x, last_x, y, last_y = 0, 1, 1, 0
        while rem:
            last_rem, (quot, rem) = rem, divmod(last_rem , rem)
            x, last_x = last_x - quot*x, x
            y, last_y = last_y - quot*y, y
        return (last_rem , last_x * (-1 if totient < 0 else 1), last_y * (-1 if totient < 0 else 1))

    def modinv(self):

        e = encryption.public_exponent
        totient = encryption.totient(self)

        g, x, y = encryption.private(self)
        if g != 1:
            raise ValueError
        return x % totient

    def public_key(self):
        return(self.primes[0]*self.primes[1], encryption.public_exponent(self))


    def private_key(self):
        return(self.primes[0]*self.primes[1], encryption.modinv(self))
