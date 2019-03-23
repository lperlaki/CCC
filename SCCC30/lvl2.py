import math
from point import ColorPoint
from util import read, write
import numpy as np


def distance(p1, p2):
    return math.sqrt(sum((p1 - p2) ** 2))


def load(nr):
    data = read(2, nr)
    rows, cols = map(int, data[0].split())
    a = []
    for row in data[1:1+rows]:
        rdata = []
        citer = iter(map(int, row.split()))
        for r in citer:
            rdata.append(ColorPoint(r, next(citer), next(citer)))
        a.append(rdata)

    return a


def level2(nr):
    out = ''
    for row in load(nr):
        rowout = []
        for i in range(len(row[0:-1])):
            rowout.append(distance(row[i], row[i + 1]))
        out += f'{" ".join(map(str, map(int, rowout)))}\n'
    write(2, nr, out)


for i in range(1, 5):
    level2(i)
