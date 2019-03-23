import math
from point import ColorPoint
from util import read, write
import numpy as np


def distance(p1, p2):
    return math.sqrt(sum((p1 - p2) ** 2))


def load(nr):
    data = read(1, nr)
    lines = int(data[0])
    a = []
    for row in data[1:1+lines]:
        rdata = []
        citer = iter(map(int, row.split()))
        for r in citer:
            rdata.append(ColorPoint(r, next(citer), next(citer)))
        a.append(rdata)

    return a


def level1(nr):
    out = ''
    for row in load(nr):
        out += f'{int(distance(row[0], row[1]))}\n'
    write(1, nr, out)


# for i in range(1, 5):
#     level1(i)


