import numpy as np

Shape = namedtuple('Shape', 'rows cols')

def read(level, nr):
    with open(f'level{level}/level{level}-{nr}.in') as f:
        return f.read()

def write(level, nr, s):
    with open(f'level{level}/level{level}-{nr}.out', 'w') as f:
        f.write(s)

def grid(shape):
    return np.arange(shape.rows * shape.cols).reshape(shape) + 1

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

    col = x
    row = y

    def __str__(self):
        return f'{self.x} {self.y}'
    

class Path(Point):
    def __init__(self, direction):
        if direction == 'N':
            super().__init__(-1, 0)
        if direction == 'S':
            super().__init__(+1, 0)
        if direction == 'E':
            super().__init__(0, +1)
        if direction == 'W':
            super().__init__(0, -1)
        
        
            
        