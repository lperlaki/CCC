import numpy as np
from point import Point
import math


def loadGrid(level, stage):
    with open(f'level{level}/level{level}_{stage}.in') as f:
        rows, cols = map(int, f.readline().rstrip().split(' '))
        d = f.read().split('\n')
        return np.array(
            list(map(lambda x: np.array(list(map(int, x.split(' ')))), d[0:rows])))


def loadPointsWithRatio(level, stage):
    with open(f'level{level}/level{level}_{stage}.in') as f:
        no = int(f.readline().rstrip())
        d = f.read().split('\n')
        ret = []
        for x in d[0:no]:
            x = tuple(map(float, x.split(' ')))
            ret.append((Point(*x[0:2]) + .5, Point(*x[2:4]) + .5, x[4]))
        return ret


def loadPoints(level, stage):
    with open(f'level{level}/level{level}_{stage}.in') as f:
        no = int(f.readline().rstrip())
        d = f.read().split('\n')
        ret = []
        for x in d[0:no]:
            x = tuple(map(float, x.split(' ')))
            ret.append((Point(*x[0:2]) + .5, Point(*x[2:4]) + .5))
        return ret


def write(level, stage, value):
    value = value if value else 0
    with open(f'level{level}/level{level}_{stage}.out', 'w') as f:
        f.write(str(value) + '\n')


def findBuildings(a):
    rows, cols = a.shape
    buidldings = []
    for row in range(rows):
        for col in range(cols):
            value = a[row, col]
            if value == 0 or value == a[row-1, col] or value == a[row, col-1]:
                continue
            start = Point(row, col)

            for i in range(row, rows):
                if value != a[i, col]:
                    for j in range(col, cols):
                        if value != a[i-1, j]:
                            end = Point(i, j) - 1
                            break
                    break
            buidldings.append((start, end, value))
    return buidldings


def level1():
    level = 1
    for stage in range(4):
        a = np.unique(loadGrid(level, stage))
        write(level, stage, ' '.join(map(str, a[a > 0])))


def level2():
    level = 2
    for stage in range(4):
        ret = []
        for c in loadPointsWithRatio(level, stage):
            a = c[0]
            b = c[1]
            r = a.pointByRatio(b, c[2])
            ret.append(r.integer())
        write(level, stage, '\n'.join(ret))


def level3():
    level = 3
    for stage in range(3):
        ret = []
        for c in loadPoints(level, stage):
            a = c[0]
            b = c[1]
            cubes = [a]
            num = int(a.distance(b))
            for i in range(1, num+1):
                r = a.pointByRatio(b, i/num)
                if all(r == a) or all(r == b):
                    continue
                cubes.append(r)
            cubes.append(b)

            ret.append(' '.join(map(lambda x: x.integer(), cubes)))
        write(level, stage, '\n'.join(ret))


def level4():
    level = 4
    for stage in range(4):
        g = loadGrid(level, stage)
        ret = []
        i = 0
        for c in findBuildings(g):
            a = c[0]
            b = c[1]
            d = (b + 1.5) - (a + .5)
            if all(abs((b+1)-a) >= 4):
                ret.append(f'{i} {(d/2 + a).integer()}')
                i += 1
        write(level, stage, ' '.join(ret))


if __name__ == "__main__":
    level4()
