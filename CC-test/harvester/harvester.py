#!/usr/bin/env python

import numpy as np


def form(a):
    return ' '.join(map(str, filter(bool, a.flat)))


def grid(rows, cols):
    return np.arange(rows * cols).reshape(rows, cols) + 1


def orient(a, start=(1, 1), dir='O'):
    if dir in 'SN':
        start = start[::-1]
        a = a.reshape(a.size, order='F').reshape(a.shape[::-1])
    if start == (1, 1):
        return a
    elif start == (a.shape[0], 1) or start == (a.shape[0] - 1, 1):
        return np.flipud(a)
    elif start == (1, a.shape[1]):
        return np.fliplr(a)
    elif start == (a.shape[0], a.shape[1]):
        return np.flip(a)


def serpentine(a):
    for i in range(1, len(a), 2):
        a[i] = np.flip(a[i])
    return a


def circle(a):
    ret = [a[0]]
    for i in range(1, len(a)//2 + 1):
        if len(ret) == len(a):
            break
        ret.append(np.flip(a[-i]))
        if len(ret) == len(a):
            break
        ret.append(a[i])
    return np.array(ret)


def dec(a, t):
    if t == 'S':
        return serpentine(a)
    elif t == 'Z':
        return circle(a)


def dual(a, e=1):
    if e == 1:
        return a
    if len(a) & 1:
        a = np.vstack((a, np.zeros((1, a.shape[1]), dtype=a.dtype)))
    ret = []
    for i in range(0, len(a), 2):
        ret.append(np.array([*map(np.array, zip(a[i], a[i+1]))]))
    return np.array(ret)


def inp(s):
    s = s.split()
    if len(s) == 2:
        return tuple(map(int, s[0:2]))
    elif len(s) == 4:
        return (tuple(map(int, s[0:2])), tuple(map(int, s[2:4])))
    elif len(s) == 5:
        return (tuple(map(int, s[0:2])), tuple(map(int, s[2:4])), s[4].upper())
    elif len(s) == 6:
        return (tuple(map(int, s[0:2])), tuple(map(int, s[2:4])), s[4].upper(), s[5].upper())
    elif len(s) == 7:
        return (tuple(map(int, s[0:2])), tuple(map(int, s[2:4])), s[4].upper(), s[5].upper(), int(s[6]))


def one():
    with open('1.txt', 'w') as f:
        for g in map(inp, ['3 4', '2 5', '5 2', '23 12']):
            f.write(form(serpentine(grid(*g))))
            f.write('\n')


def two():
    with open('2.txt', 'w') as f:
        for g in map(inp, ['3 4 1 1', '2 5 2 1', '5 2 5 2', '23 12 1 12']):
            f.write(form(serpentine(orient(grid(*g[0]), g[1]))))
            f.write('\n')


def three():
    with open('3.txt', 'w') as f:
        for g in map(inp, ['3 4 1 1 S', '2 5 1 5 S', '5 2 5 2 N', '23 12 23 1 N']):
            f.write(form(serpentine(orient(grid(*g[0]), g[1], g[2]))))
            f.write('\n')


def four():
    with open('4.txt', 'w') as f:
        for g in map(inp, ['3 4 1 4 S Z', '2 5 2 1 N S', '5 2 5 2 N Z', '23 12 23 1 N Z']):
            f.write(form(dec(orient(grid(*g[0]), g[1], g[2]), g[3])))
            f.write('\n')


def five():
    with open('5.txt', 'w') as f:
        for g in map(inp, ['5 4 1 1 O S 2', '5 4 4 1 O Z 2', '10 10 10 10 W S 1', '10 10 10 10 W S 2', '17 9 17 1 N Z 2']):
            f.write(
                form(dec(dual(orient(grid(*g[0]), g[1], g[2]), g[4]), g[3])))
            f.write('\n')


def main():
    # one()
    # two()
    # three()
    # four()
    five()


if __name__ == '__main__':
    main()
