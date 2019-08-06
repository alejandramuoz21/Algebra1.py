from Lineal import *
from numpy import *
#Ejercicio 1
a = array([[3, 0, -1], [-7/5, 2, -1], [-1, 1, (-7/5 + 1)]], float)
print(a)
b = array([[5], [2], [1]], float)
print(b)
c = concatenate([a, b], axis=1)
print(c)
c[0, 0:] = c[0, 0:] / c[0, 0]
print(c)
c[1, 0:] = c[1, 0:] - c[1, 0] * c[0, 0:]
c[2, 0:] = c[2, 0:] - c[2, 0] * c[0, 0:]
print(c)
c[1, 1:] = c[1, 1:] / c[1, 1]
print(c)
c[0, 1:] = c[0, 1:] - c[0, 1] * c[1, 1:]
c[2, 1:] = c[2, 1:] - c[2, 1] * c[1, 1:]
print(c)
c[2, 2:] = c[2, 2:] / c[2, 2]
print(c)
c[0, 2:] = c[0, 2:] - c[0, 2] * c[2, 2:]
c[1, 2:] = c[1, 2:] - c[1, 2] * c[2, 2:]
print(c)
x = c[:, 3]
print(x)

x = gaussjordan1(a, b)
print(x)
r = dot(a, x)
print(r)

#Ejercicio 2
from Lineal import *
a = array([[1/2, 1/3, 1/4], [2/3, 2/4, 2/5], [3/4, 3/5, 3/6]], float)
b = array([[2], [4], [6]], float)
c = concatenate([a, b], axis=1)
print(c)
print(gaussjordan1(a, b))

from GaussBasico import *
a = array([[1/2, 1/3, 1/4, 1/5], [2/3, 2/4, 2/5, 2/6], [3/4, 3/5, 3/6, 3/7], [4/5, 4/6, 4/7, 4/8]], float)
b = array([[2], [4], [6], [8]], float)
c = concatenate([a, b], axis=1)
print(c)
x = gauss1(a, b)
print(x)

#Ejercicio 3
from Lineal import *
a = array([[1, 1/2, 1/3], [1/4, 1/5, 1/6], [1/7, 1/8, 1/9]], float)
b = array([[4], [5], [6]], float)
c = concatenate([a, b], axis=1)
print(c)
x = gaussjordan2(a, b)
print(x)
print(inversa(a, b))

#Ejercicio 4
from numpy import *
a = array([[0.52, 0.30, 0.18], [0.20, 0.50, 0.30], [0.25, 0.20, 0.55]], float)
b = array([[0.6], [0.5], [0.4]], float)
c = concatenate([a, b], axis=1)
print(c)

from Jacobi import *
x = array([[1], [1], [1]], float)
x = jacobi(a, b, x); print(x)
x = jacobi(a, b, x); print(x)
x = jacobi(a, b, x); print(x)
x = jacobi(a, b, x); print(x)
x = jacobi(a, b, x); print(x)
x = jacobi(a, b, x); print(x)
x = jacobi(a, b, x); print(x)

from GaussSeidel import *
x = array([[1], [1], [1]], float)
x = gaussseidel(a, b, x); print(x)
x = gaussseidel(a, b, x); print(x)
x = gaussseidel(a, b, x); print(x)
x = gaussseidel(a, b, x); print(x)

from GaussSeidel import *
x = array([[1], [1], [1]], float)
[x, k] = gaussseidelm(a, b, x, 0.0001, 20)
print(x)
print(k)

#Ejercicio 5
from numpy import *
a = array([[4, 2, 5], [2, 5, 1], [2, 4, 3]], float)
b = array([[18], [27.30], [16.20]], float)
c = concatenate([a, b], axis=1)
print(c)

from Jacobi import *
x = array([[1], [1], [1]], float)
x = jacobi(a, b, x); print(x)
x = jacobi(a, b, x); print(x)
x = jacobi(a, b, x); print(x)
x = jacobi(a, b, x); print(x)
x = jacobi(a, b, x); print(x)
x = jacobi(a, b, x); print(x)
x = jacobi(a, b, x); print(x)

from GaussSeidel import *
x = array([[1], [1], [1]], float)
x = gaussseidel(a, b, x); print(x)
x = gaussseidel(a, b, x); print(x)
x = gaussseidel(a, b, x); print(x)
x = gaussseidel(a, b, x); print(x)
x = gaussseidel(a, b, x); print(x)

from GaussSeidel import *
x = array([[1], [1], [1]], float)
[x, k] = gaussseidelm(a, b, x, 0.0001, 20)
print(x)
print(k)
