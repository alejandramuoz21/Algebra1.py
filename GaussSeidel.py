def gaussseidel(a, b, x):
    n = len(x)
    for i in range(n):
        s = 0
        for j in range(n):
            if i!= j:
                s = s + a[i, j] *x[j]
        x[i] = (b[i] - s) / a[i, i]
    return x


import numpy as np
def gaussseidelm(a, b, x, e, m):
    n = len(x)
    t = x.copy()
    for k in range(m):
        x = gaussseidel(a, b, x)
        d = np.linalg.norm(np.array(x) - np.array(t))
        if d<e:
            return [x, k]
        else:
            t = x.copy()
    return [[], m]