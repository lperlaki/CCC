#!/bin/env python3

def inFile(path):
    samples = []
    with open(path + '.inp', 'r') as f:
        for i in range(int(f.readline())):
            infoline = f.readline().split()
            info = { 'timestamp': int(infoline[0]), 'row': int(infoline[1]), 'col': int(infoline[2]), 'grid': []}
            for r in range(info['row']):
                info['grid'].append(list(map(int,f.readline().split())))
            samples.append(info)
    return samples


def hasColor(samp):
    return any(j for i in samp['grid'] for j in i)


def lvl1(path):
    samples = inFile(path)
    with open(path + '.out', 'w') as f:
        for samp in samples:
            if hasColor(samp):
                f.write('{}\n'.format(samp['timestamp']))

for i in range(3):
    lvl1('lvl1-{}'.format(i))

