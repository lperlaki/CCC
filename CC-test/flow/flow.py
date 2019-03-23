import numpy as np
from munch import Munch
import pandas as pd
from collections import namedtuple
array = np.array


def form(i):
    return ' '.join(map(str, i))


Shape = namedtuple('Shape', 'rows cols')


class Point(np.ndarray):
    def __new__(cls, *args, **kwargs):
        return np.ndarray(2, int).view(cls)

    def __init__(self, x=0, y=0, color=None):
        self.x = x
        self.y = y
        self.color = color

    @classmethod
    def fromIndex(cls, index, shape, *args, **kwargs):
        return cls(x=(index - 1) // shape.cols + 1, y=(index - 1) % shape.cols + 1, *args, **kwargs)

    @property
    def x(self):
        return self[0]

    @x.setter
    def x(self, value):
        self[0] = value

    @property
    def y(self):
        return self[1]

    @y.setter
    def y(self, value):
        self[1] = value

    row = x
    col = y

    def __str__(self):
        return f'{self.x} {self.y}'


p = Point(1, 2,)


def grid(shape):
    return np.arange(shape.rows * shape.cols).reshape(shape) + 1


class Data:
    def __init__(self, s):
        self.data = tuple(map(int, s.split()))
        self.shape = Shape(self.data[0], self.data[1])
        self.grid = grid(self.shape)

    def p1(self):
        self.points = list(map(lambda x: Point.fromIndex(
            x, self.shape), self.data[3: self.data[2] + 3]))
        return self

    def p2(self):
        it = iter(self.data[3: self.data[2]*2 + 3])
        self.points = list(map(lambda x: Point.fromIndex(
            x, self.shape, color=next(it)), it))
        return self


def colorZip(points):
    s = sorted(points, key=lambda x: x.color)
    return list(zip(s[0::2], s[1::2]))


def manahtan(a, b):
    return sum(abs(a - b))


def read(level, nr):
    with open(f'level{level}/level{level}-{nr}.in') as f:
        return Data(f.read())


def write(level, nr, s):
    with open(f'level{level}/level{level}-{nr}.out', 'w') as f:
        f.write(s)


def l1():
    for n in range(4):
        write(1, n, ' '.join(map(str, read(1, n).p1().points)))


def l2():
    for n in range(4):
        m = read(2, n).p2()
        write(2, n, ' '.join(map(str, map(lambda x: manahtan(*x), colorZip(m.points)))))


