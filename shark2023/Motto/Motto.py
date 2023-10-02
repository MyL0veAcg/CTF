flag = b'SharkCTF{xxxxxxxxxxxxxx}'    

key = [int.from_bytes(b'The Wisdom ', 'big'),
       int.from_bytes(b'That Nurtures', 'big'),
       int.from_bytes(b' Everything', 'big')]
def golden_sentence(i):
    if i == 0:
        return key[0]
    elif i == 1:
        return key[1]
    elif i == 2:
        return key[2]
    else:
        return (golden_sentence(i - 1) +
                golden_sentence(i - 2) * 3 +
                golden_sentence(i - 3) * 5) % 256


enc = b''
for i in range(len(flag)):
    letter = golden_sentence((i//2) ** 8) % 256
    enc += bytes([letter ^ flag[i]])
print(f"enc={enc}")
"""
enc=b"sH\x12\x01Kc\xc7\xd5[A\xbd\xb7\x7fbV]\x13F\xda\xc7\x15\x7f';E\x7fD#R\x11\x97\x8e"
"""
