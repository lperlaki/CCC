import math
from point import ColorPoint
from util import read, write
import numpy as np
import sys


sys.setrecursionlimit(10000)


def distance(p1, p2):
    return int(math.sqrt(sum((p1 - p2) ** 2)))


def load(nr):
    data = read(3, nr)
    rows, cols = map(int, data[0].split())
    startRow, startCol = map(int, data[1].split())
    a = []
    for row in data[2:2+rows]:
        rdata = []
        citer = iter(map(int, row.split()))
        for r in citer:
            rdata.append(ColorPoint(r, next(citer), next(citer)))
        a.append(rdata)

    return (np.array(a), (startRow, startCol))


def cInRange(shape, cord):
    return 0 <= cord[0] < shape[0] and 0 <= cord[1] < shape[1]


def go(a, pos, visited=set()):
    visited.add(pos)
    pup = (pos[0]+1, pos[1])
    pdown = (pos[0]-1, pos[1])
    pright = (pos[0], pos[1]+1)
    if not cInRange(
            a.shape[0:2], pos):
        return[]
    cup = distance(a[pos], a[pup]) if cInRange(
        a.shape[0:2], pup) and pup not in visited else math.inf
    cdown = distance(a[pos], a[pdown]) if cInRange(
        a.shape[0:2], pdown) and pdown not in visited else math.inf
    cright = distance(a[pos], a[pright]) if cInRange(
        a.shape[0:2], pright) and pright not in visited else math.inf
    m = min((cup, cright, cdown))
    if m == math.inf:
        return[pos]
    elif m == cdown:
        return [pos, *go(a, pdown)]
    elif m == cright:
        return [pos, *go(a, pright)]
    elif m == cup:
        return [pos, *go(a, pup)]

    else:
        return [pos]


def level3(nr):
    write(3, nr, '\n'.join(map(lambda x: ' '.join(map(str, x)), go(*load(nr)))))


if __name__ == '__main__':
    for i in range(4, 5):
        level3(i)
