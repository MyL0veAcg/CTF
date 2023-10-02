import numpy as np
 
enc=b"sH\x12\x01Kc\xc7\xd5[A\xbd\xb7\x7fbV]\x13F\xda\xc7\x15\x7f';E\x7fD#R\x11\x97\x8e"
key = [int.from_bytes(b'The Wisdom ', 'big'),
       int.from_bytes(b'That Nurtures', 'big'),
       int.from_bytes(b' Everything', 'big')]
flag = []
# 定义矩阵 A
X = [key[2], key[1], key[0]]
A = [[1, 1, 0],
     [3, 0, 1],
     [5, 0, 0]]
X = np.matrix(X)
A = np.matrix(A)

def golden_sentence(i):
    if i == 0:
        return key[0]
    elif i == 1:
        return key[1]
    elif i == 2:
        return key[2]
    else:
        ans = X*(A**(i-2))
        return ans.tolist()[0][0]


flag = b''
for i in range(len(enc)):
    letter = golden_sentence((i//2) ** 8) % 256
    flag += bytes([letter ^ enc[i]])
print(f"flag={flag}")