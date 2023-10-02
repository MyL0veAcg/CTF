from Crypto.Util.number import *
from challenges.secret import gift1


class RSAServe:
    def __init__(self) -> None:
        def create_keypair(size):
            p = getPrime(size // 2)
            q = getPrime(size // 2)
            N = p * q
            phi = (p - 1) * (q - 1)
            e = 0x10001
            d = inverse(e, phi)
            return p, q, N, e, d
        self.p, self.q, self.N, self.e, self.d = create_keypair(1024)
        self.m = gift1

    def encrypt(self):
        m_ = bytes_to_long(self.m)
        c = pow(m_, self.e, self.N)
        return hex(c)

    def check(self, msg):
        return msg == self.m

    def pubkey(self):
        return {"p": self.p, "q": self.q, "e": self.e}
