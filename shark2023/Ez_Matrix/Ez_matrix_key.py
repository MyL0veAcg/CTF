from Crypto.Util.number import *
from sympy import Matrix

A = Matrix([
    [8, 9, 5],
    [4, 0, 5],
    [7, 5, 6],
])
B = Matrix([[3464621843199187888196794459432008261], [1732310921599593944098397773374358865], [3031544112799289402172195505470241914]])
X = A **(-1) * B
print(X)
X = list(X)
print(X)
for m in X:
    print(long_to_bytes(m))