import math
import numpy as np
y = np.array([[0.375,0.0625,0.03125,0],[0.0625,0.125,0.03125,0.0625],[0.0625,0.0625,0.0625,0.0625],[0.0,0.0,0.0,0.0]])
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
t = 0
xjk = 0
hx1 = 0
j = 0
while j <= 3:
    if h1x[j] != 0:
        xjk += h1x[j] * -(math.log(h1x[j],2))
    j += 1
    hx1 = xjk
hx2 = 0
jkl = 0
g = 0
while g <= 3:
    if h1y[g] != 0:
        jkl += h1y[g] * -(math.log(h1x[g],2))
    g += 1
    hx2 = jkl
print(hx1)
print(hx2)
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
hx1y = hxy - hx1
hy1x = hxy - hx2
print(hx1y)
print(hy1x)