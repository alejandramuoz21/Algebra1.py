from numpy import *
a = array([[2, 4, 5], [3, 1, 4], [5, 2, 4]], float)
b = array([[5], [6], [7]], float)
linalg.det(a)

x = dot(linalg.inv(a), b)
print(x)

set_printoptions(precision = 4)
print(x)

r = dot(a, x)
print(r)

x = linalg.solve(a, b)
print(x)


import numpy as np
a = np.array([[2, 4, 5], [3, 1, 4], [5, 2, 4]], float)
np.linalg.det(a)