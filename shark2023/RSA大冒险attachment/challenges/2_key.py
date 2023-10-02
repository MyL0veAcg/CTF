from Crypto.Util.number import *

N = 2974433245416937199771772194581747
p = 54407728068195407
q = 54669315390062621
e = 65537
c = 0x56638d0e09e2fd310f49f5626095

phi = (p-1)*(q-1)
d = inverse(e, phi)
m = pow(c, d, N)
print(long_to_bytes(m))
