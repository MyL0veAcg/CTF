from Crypto.Util.number import *
from sympy import Matrix
from secret import flag

m = flag.split(b'_')
X = [bytes_to_long(i) for i in m]
A = Matrix([
    [8, 9, 5],
    [4, 0, 5],
    [7, 5, 6],
])
B = A * Matrix(X)
print(B)
'''
Matrix([[3464621843199187888196794459432008261], [1732310921599593944098397773374358865], [3031544112799289402172195505470241914]])
'''
