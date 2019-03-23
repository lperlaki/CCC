import numpy


def getArgs(args):
    return (0,) if not args else args[0] if len(args) == 1 and hasattr(
        args[0], "__iter__") else args


class Point(numpy.ndarray):
    def __new__(cls, *args, dtype=None, **kwargs):
        args = getArgs(args)
        dtype = dtype if dtype else type(args[0])
        return numpy.ndarray(len(args), dtype).view(cls)

    def __init__(self, *args, **kwargs):
        args = getArgs(args)
        for i in range(len(args)):
            self[i] = args[i]

    @classmethod
    def zeros(cls, ndim=1):
        return cls([0]*ndim)

    @classmethod
    def ones(cls, ndim=1):
        return cls([1]*ndim)

    @property
    def s(self):
        return tuple(self)

    _ = s

    @property
    def x(self):
        return self[0]

    @x.setter
    def x(self, value):
        self[0] = value

    row = x

    @property
    def y(self):
        return self[1] if self.shape[0] >= 2 else None

    @y.setter
    def y(self, value):
        if self.shape[0] >= 2:
            self[1] = value

    col = y

    @property
    def z(self):
        return self[2] if self.shape[0] >= 3 else None

    @z.setter
    def z(self, value):
        if self.shape[0] >= 3:
            self[2] = value

    def __str__(self):
        return ' '.join(map(str, self))

    def int(self):
        return self.astype(int)

    def distance(self, other):
        return numpy.sqrt(numpy.sum((self-other) ** 2))

    def area(self, other):
        return numpy.prod(numpy.array(numpy.abs(self - other)))

    def pointByRatio(self, other, ratio=.5):
        return (other - self) * ratio + self
