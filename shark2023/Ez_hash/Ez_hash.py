import string
import random
from hashlib import *
from secret import flag

table = string.digits + string.ascii_letters
flag = b'SharkCTF{XXXX_XXXX_XXXX_XXXX}'
flag = flag[9:-1].split(b'_')

for f in flag:
    assert len(f) == 4                             #不用看

hash_enc = []
res = []


def hash_encode(m):
    proof = (''.join([random.choice(table) for _ in range(10)])).encode()   #从table中随机抽10个组成proof
    res.append(proof)
    c = sha256(m + proof).hexdigest().encode()                              #用proof结合哈希加密
    hash_enc.append(c)


for m in flag:
    hash_encode(m)                                                        #flag分成四段，一个proof和一个hash_enc对应
print(f'res={res}')
print(f'hash_enc={hash_enc}')
'''
res = [b'ASwwBYb4as', b'90I9Md9Gvq', b'nVmQJxmadm', b'qzt2xog1Xj']
hash_enc = [b'971d92427e0f5e36576248b52c67438f0fe36a1c8677f73103c7789dcbd01969', b'8c0e686cbb00002dc933462e10a455c1201f565733c8113fc0cfcbcb1de3021a',
            b'bb180e0b0e8ce912847895f89e021a25f107fb53d2ac20de6d86466033b02954', b'6dd2f1822b7018ecfa16fc38eab015d3cdca5ade66af24df7da22627f7d31527']
'''
