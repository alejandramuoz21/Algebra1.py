import numpy as np
def gauss1(a,b):
    n = len(b)
    c = np.concatenate([a,b], axis=1)
    for e in range(n):
        t = c[e, e]
        for j in range(e, n + 1):
            c[e, j] = c[e, j] / t
        for i in range(n):
            if i != e:
                t = c[i, e]
                for j in range(e, n + 1):
                    c[i, j] = c[i, j]-t*c[e, j]
    x = np.zeros([n, 1])
    x[n - 1] = c[n - 1, n]
    for i in range(n - 2, -1, -1):
        s = 0
        for j in range(i + 1, n):
            s = s + c[i, j] * x[j]
        x[i] = c[i, n] - s
    return x


def gauss2(a,b):
    n = len(b)
    c = np.concatenate([a,b], axis=1)
    for e in range(n):
        c[e, e:] = c[e, e:] / c[e, e]
        for i in range(e + 1, n):
            c[i, e:] = c[i, e] - c[i, e] * c[e, e:]
    x = np.zeros([n, 1])
    x[n - 1] = c[n - 1, n]
    for i in range(n - 2, -1, -1):
        x[i] = c[i, n] - np.dot(x[i + 1: n], c[i, i + 1: n])
    return x