from Lineal import *
from numpy import *
a = array([[4, 2, 5], [2, 5, 8], [2, 4, 3]], float)
b = array([[18.00], [27.3], [16.2]], float)

print(gaussjordan1(a,b))

print(gaussjordan2(a,b))

print(inversa(a,b))