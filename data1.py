import math
from typing import Any

import numpy as np
from numpy import ndarray, dtype

y = np.array([[0.125,0.0625,0.03125,0.03125],[0.0625,0.125,0.03125,0.03125],[0.0625,0.0625,0.0625,0.0625],[0.25,0,0,0]])
i = 0
h1y = np.array([0.0,0.0,0.0,0.0])
while i <= 3:
    j = 0
    hx = 0
    while j <= 3:
        hx += y[i,j]
        h1y[i] = hx
        j += 1
    i += 1
print(h1y)
h1x = np.array([0.0,0.0,0.0,0.0])
x = 0
while x <= 3:
    j = 0
    hx = 0
    while j <= 3:
        hx += y[j,x]
        h1x[x] = hx
        j += 1
    x += 1
print(h1x)
def niubi(date):
    m = 0
    n = 0
    while m <= 3:
        n += (date[m] * -(math.log(date[m], 2)))
        m += 1
    return n
res1 = niubi(h1y)
res2 = niubi(h1x)
print(res1)
print(res2)
hxy = 0
k = 0
num = 0
while k <= 3:
    j = 0
    while j <= 3:
        if y[k,j] != 0:
            num += y[k,j] * -(math.log(y[k,j],2))
        j += 1
    k += 1
    hxy = num
print(hxy)
hx1y = hxy - res1
hy1x = hxy - res2
print(hx1y)
print(hy1x)