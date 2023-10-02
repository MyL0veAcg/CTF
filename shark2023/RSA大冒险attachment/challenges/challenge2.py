from Crypto.Util.number import *
from challenges.secret import gift2


class RSAServe:
    def __init__(self) -> None:
        def creat_keypair(nbits):
            p = getPrime(nbits // 2)
            q = getPrime(nbits // 2)
            N = p * q
            phi = (p-1) * (q-1)
            e = 0x10001
            d = inverse(e, phi)
            return N, e, d
        self.N, self.e, self.d = creat_keypair(112)
        self.m = gift2

    def encrypt(self):
        m_ = bytes_to_long(self.m)
        c = pow(m_, self.e, self.N)
        return hex(c)

    def check(self, msg):
        return msg == self.m

    def pubkey(self):
        return {"N": self.N, "e": self.e}
