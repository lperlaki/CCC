import sys
import math

sys.setrecursionlimit(2000)

import numpy as np


def load(level, stage):
    with open(f'level{level}/level{level}_{stage}.in') as f:
        d = f.read().split('\n')
        rows, cols = map(int, d[0].split(' '))
        return np.array(
            list(map(lambda x: np.array(list(map(int, x.split(' ')))), d[1:rows+1])))


def loadPairs(level, stage):
    with open(f'level{level}/level{level}_{stage}.in') as f:
        d = f.read().split('\n')
        rows, cols = map(int, d[0].split(' '))
        pairs = int(d[rows+1])
        return list(map(lambda x: tuple(map(int, x.split(' '))), d[rows+2: rows + 2 + pairs]))


def write(level, stage, value):
    with open(f'level{level}/level{level}_{stage}.out', 'w') as f:
        f.write(str(value))


def findBuildings(a):
    done = np.zeros(a.shape)
    rows, cols = a.shape
    buidldings = []
    for i in range(rows):
        for j in range(cols):
            value = a[i, j]
            if value == 0 or (done[i, j]):
                continue
            buidldings.append((area(a, done, value, (i, j), [])))
    return buidldings


def buidlingCenter(a):
    u = np.unique(a)
    u = u[u != 0]
    done = np.zeros(a.shape)
    rows, cols = a.shape
    buidldings = []
    for i in range(rows):
        for j in range(cols):
            value = a[i, j]
            if value == 0 or (done[i, j]):
                continue
            cords = []
            n = (area(a, done, value, (i, j), cords))
            cords = list(map(list, zip(*cords)))
            x = sum(cords[0])
            y = sum(cords[1])
            buidldings.append((x/n, y/n))
    return buidldings


def area(a, done, value,  cord, coordinates):
    bounds = cord[0] < 0 or cord[0] > a.shape[0] - \
        1 or cord[1] < 0 or cord[1] > a.shape[1] - 1
    if bounds or a[cord] != value or done[cord]:
        return 0

    done[cord] = 1
    coordinates.append(cord)
    return\
        area(a, done, value, (cord[0] - 1, cord[1]), coordinates) + \
        area(a, done, value, (cord[0] + 1, cord[1]), coordinates) +\
        area(a, done, value, (cord[0], cord[1] - 1), coordinates) +\
        area(a, done, value, (cord[0], cord[1] + 1), coordinates) + 1


def level1():
    for i in range(5):
        write(1, i, int(load(1, i).any()))


def level2():
    for i in range(5):
        write(2, i, ' '.join(map(lambda x: f'{x[0]} {x[1]}',
                                 enumerate(sorted(findBuildings(load(2, i)))))))


def level3():
    for i in range(5):
        bu = dict(enumerate(sorted(buidlingCenter(load(3, i)))))
        di = ''
        for a, b in loadPairs(3, i):
            a = bu[a]
            b = bu[b]
            dx = a[0] - b[0]
            dy = a[1] - b[1]
            d = math.sqrt(dx ** 2 + dy ** 2)
            di += f'{math.ceil(d)}\n'

        write(3, i, di)


if __name__ == '__main__':
    level3()
