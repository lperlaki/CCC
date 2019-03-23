#!/bin/env python3

from collections import namedtuple
import numpy as np

Meta = namedtuple('Meta', 'start end count samples')

class Sample():
    def __init__(self, timestamp, row, col):
        self.timestamp = int(timestamp)
        self.row = int(row)
        self.col = int(col)

    def notNull(self):
        return self.grid.any()
        


def inFile(path):
    with open(path + '.inp', 'r') as f:
        first = f.readline().split()
        meta = Meta(int(first[0]), int(first[1]), int(first[2]), [])
        for i in range(meta.count):
            infoline = f.readline().split()
            sample = Sample(infoline[0], infoline[1], infoline[2])
            grid = []
            for r in range(sample.row):
                grid.append(list(map(int,f.readline().split())))
            sample.grid = np.array(grid)
            meta.samples.append(sample)
    return meta





def lvl1(path):
    meta = inFile(path)
    with open(path + '.out', 'w') as f:
        for samp in meta.samples:
            if samp.notNull():
                f.write('{}\n'.format(samp.timestamp))

for i in range(5):
    lvl1('lvl1-{}'.format(i))
