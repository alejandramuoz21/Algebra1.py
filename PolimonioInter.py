from Lagrange import *
x = [2, 4, 5]
y = [5, 6, 3]
p = lagrange(x, y)
print(p)
r = lagrange(x, y, 4.25)
print(r)
r = lagrange(x, y, [3.15, 3.74, 4.25])
print(r)


import pylab as pl
u = pl.arange(2, 5.1, 0.1)
v = lagrange(x, y, list(u))
pl.plot(u, v)
pl.plot(x, y, 'o')
pl.grid(True)
pl.show()
