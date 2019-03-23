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


def pairSamples(samples):
    ret = []
    samp = iter(samples)
    for front in samp:
        met = {'timestamp': front['timestamp'], 'front': front['grid'], 'back': map(lambda x: list(reversed(x)), next(samp)['grid'])}

        ret.append(met)
    return ret


def addFB(samp):
    ret = []
    for i in range(len(samp['front'])):
        ret.append([])
        for j in range(len(samp['front'][i])):
            ret[i].append(samp['front'][i][j] + samp['back'][i][j])
    return ret

def subIdNotNull(x, y):
    if y != 0:
        return x - y
    return 0

def lvl3(path):
    samples = pairSamples(inFile(path))
    with open(path + '.out', 'w') as f:
        for s in samples:
            dif = addFB(s)
            ma = max(j for i in dif for j in i) + 1
            dif2 = map(lambda x: map(lambda y: subIdNotNull(ma, y), x), dif)
            ret = sum(j for i in dif2 for j in i)
            f.write('{} {}\n'.format(s['timestamp'], ret))
        




for i in range(5):
    lvl3('lvl3-{}'.format(i))

