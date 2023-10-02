from Crypto.Util.number import *
from challenges.secret import gift3


class RSAServe:
    def __init__(self) -> None:
        def create_keypair(nbits):
            e = 3
            while True:
                p = getPrime(nbits // 2)
                q = getPrime(nbits // 2)
                phi = (p-1) * (q-1)
                if GCD(e, phi) == 1:
                    break
            N = p * q
            d = inverse(e, phi)
            return N, e, d
        self.N, self.e, self.d = create_keypair(540)
        self.m = gift3

    def encrypt(self):
        m_ = bytes_to_long(self.m)
        c = pow(m_, self.e, self.N)
        return hex(c)

    def check(self, msg):
        return msg == self.m

    def pubkey(self):
        return {"e": self.e}
