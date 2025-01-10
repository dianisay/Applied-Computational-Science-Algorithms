
import numpy as np
from random import random, gauss

def f(x1, x2, x3):
    return x1 + 2 * x2 + x2 * x3 - x1 * x1 - x2 * x2 - x3 * x3

def mutation(x, s):
    xn = x + s * gauss(0, 1)
    while xn < -2 or xn > 2:
        xn = x + s * gauss(0, 1)
    return xn

def sigma(s, g, m):
    ps = m / g
    c = 0.817
    if g % 20 == 0:
        if ps > 0.2:
            s = s / c
        elif ps < 0.2:
            s = s * c
    return s

def main():
    xmin, xmax = -2, 2
    gmax = 500
    m = 0
    c = 0.817
    x = [4 * random() + xmin, 4 * random() + xmin, 4 * random() + xmin]
    x0 = [round(xi, 6) for xi in x]
    print("x0: ", x0)
    parent = f(*x)
    s = 1
    path = [x]
    for g in range(1, gmax):
        xn = [mutation(xi, s) for xi in x]
        child = f(*xn)
        if child > parent:
            x = xn
            m += 1
            parent = child
        s = sigma(s, g, m)
        path.append(x)
    xf = [round(xi, 6) for xi in x]
    print("xf: ", xf)

main()
