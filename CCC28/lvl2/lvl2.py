#!/bin/env python3

from collections import namedtuple
import numpy as np

Meta = namedtuple('Meta', 'start end count samples')

def norm(zahl):
    if zahl == 0:
        return 0
    return 1


def crop(arr):
    return arr[[slice(*a) for a in [(min(a), max(a)+1) for a in np.nonzero(arr)]]]



class Sample():
    def __init__(self, timestamp, row, col):
        self.timestamp = int(timestamp)
        self.row = int(row)
        self.col = int(col)

    def isEmpty(self):
        return self.grid.any()

    def crop(self):
        return crop(self.grid)

    def __repr__(self):
        return "timestamp: {} row: {} col: {} grid:\n{}".format(self.timestamp, self.row, self.col, str(self.grid))

    def normalize(self):
        result = np.empty(self.grid.shape)
        for i in range(len(self.grid.flat)):
            result.flat[i] = norm(self.grid.flat[i])
        return result
        
    def compShape(self, other):
        sel = crop(self.normalize())
        oth = crop(other.normalize())
        return np.all(sel==oth)




def removeEmpty(samp):
    return list(filter(lambda x: x.isEmpty(), samp))

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

def getSame(samp, samples):
    ret = []
    for s in samples:
        if samp.compShape(s):
            ret.append(s)
    return ret



def lvl2(path):
    meta = inFile(path)
    samples = removeEmpty(meta.samples)
    with open(path + '.out', 'w') as f: 
        al = []
        for s in samples:
            o = getSame(s, samples)
            if o not in al:
                al.append(o)
        for e in al:
            f.write('{} {} {}\n'.format(min(map(lambda x: x.timestamp, e)), max(map(lambda x: x.timestamp, e)), len(e)))

def main():
    for i in range(5):
        lvl2('lvl2-{}'.format(i))

main()




