import math
from point import ColorPoint
from util import read, write
import numpy as np

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