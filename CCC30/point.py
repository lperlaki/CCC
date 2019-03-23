import numpy as np


class Point(np.ndarray):
    def __new__(cls, *args, **kwargs):
        return np.ndarray(2, int).view(cls)

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def I(self):
        return tuple(self)

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

    def __str__(self):
        return f'{self.x} {self.y}'
