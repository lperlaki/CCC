import numpy as np


class ColorPoint(np.ndarray):
    def __new__(cls, *args, **kwargs):
        return np.ndarray(3, int).view(cls)

    def __init__(self, r=0, g=0, b=0):
        self.r = r
        self.g = g
        self.b = b

    @property
    def r(self):
        return self[0]

    @r.setter
    def r(self, value):
        self[0] = value

    @property
    def g(self):
        return self[1]

    @g.setter
    def g(self, value):
        self[1] = value

    @property
    def b(self):
        return self[2]

    @b.setter
    def b(self, value):
        self[2] = value

    def __str__(self):
        return f'{self.r} {self.g} {self.b}'
