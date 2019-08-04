import numpy as np
def gauss(a, b):
    n = len(b)
    c = np.concatenate([a, b], axis = 1)

    for e in range(n):
        p = e
        for i in range(e + 1, n):
            if abs(c[i, e])> abs(c[p, e]):
                p = i

        for j in range(e, n + 1):
            t = c[e, j]
            c[e, j] = c[p, j]
            c[p, j] = t

        t = c[e, e]
        if abs(t) < 1e-20:
            return []

        c[e, e: ] = c[e, e: ] / c[e, e]
        for i in range(e + 1, n):
            c[i, e:] = c[i, e:] - c[i, e] * c[e, e:]

    x = np.zeros([n])
    x[n - 1] = c[n -1, n]
    for i in range(n - 2, -1, -1):
        x[i] = c[i, n] - np.dot(x[i + 1:n], c[i, i + 1:n])
    return x