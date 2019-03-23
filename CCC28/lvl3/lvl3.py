#!/bin/env python3

from collections import namedtuple
import numpy as np

Meta = namedtuple('Meta', 'start end count samples')

def norm(zahl):
    if zahl == 0:
        return 0
    return 1


def crop(arr):
    return arr[[slice(*a) for a in [(min(a), max(a)+1) for a in arr.nonzero()]]]



class Sample():
    def __init__(self, timestamp, row, col):
        self.timestamp = int(timestamp)
        self.row = int(row)
        self.col = int(col)

    def isNotEmpty(self):
        return self.grid.any()

    def crop(self):
        return crop(self.grid)

    def __repr__(self):
        return "timestamp: {} row: {} col: {} grid:{}".format(self.timestamp, self.row, self.col, str(self.grid))

    def normalize(self):
        return np.array(np.ceil(self.grid / (self.grid + 1)), dtype=int)
        
    def __eq__(self, other):
        sel = crop(self.normalize())
        oth = crop(other.normalize())
        return np.all(sel==oth)

    def getInterval(self, other):
        return other.timestamp - self.timestamp





def removeEmpty(samp):
    return list(filter(lambda x: x.isNotEmpty(), samp))

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
        if samp == s:
            ret.append(s)
    return ret

def getSubset(samples):
    ret = []
    for i in range(len(samples)):
        intervals = [s.timestamp - samples[i].timestamp for s in samples[i:]][1:]
        for inter in intervals:
            sup = []
            intu = [inter * asd for asd in range(1,4)]
            for sample in samples[i:]:
                if sample.timestamp < multi * inter + samples[i].timestamp:
                    continue
                elif sample.timestamp == multi * inter + samples[i].timestamp:
                    sup.append(sample)
                break
            if len(sup) > 3:
                ret.append(sup)
    return ret







def lvl3(path):
    meta = inFile(path)
    samples = removeEmpty(meta.samples)
    with open(path + '.out', 'w') as f: 
        al = []
        for s in samples:
            o = getSame(s, samples)
            if o not in al and len(o) > 3:
                al.append(o)
        for e in al:
            a = getSubset(e)
            for b in a:
                print(a)
                #f.write('{} {} {}\n'.format(min(map(lambda x: x.timestamp, b)), max(map(lambda x: x.timestamp, b)), len(b)))

def main():
    for i in range(1):
        lvl3('lvl3-{}'.format(i))

if __name__ == '__main__':
    main()



