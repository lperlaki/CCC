from util import read
from numpy import array
from point import Point


def intList(l):
    return list(map(int, l))


def strList(l):
    return list(map(str, l))


def strToArr(s):
    return array(intList(s.split()))


def lvl1(nr):
    inp = read(1, nr).split('\n')
    start = Point(*intList(inp[0].split()))
    args = inp[1].split()
    commands = list(zip(args[0::2], intList(args[1::2])))
    return (start, commands)


def lvl2(nr):
    inp = read(2, nr).split('\n')
    world = intList(inp[0].split())
    start = Point(*intList(inp[1].split()))
    args = inp[2].split()
    commands = list(zip(args[0::2], intList(args[1::2])))
    return (start, commands)


def lvl3(nr):
    inp = read(3, nr).split('\n')
    world = intList(inp[0].split())
    start = Point(*intList(inp[1].split()))
    args = inp[2].split()
    commands = list(zip(args[0::2], intList(args[1::2])))
    speed = float(inp[3])
    n_alien = int(inp[4])
    aliens = intList(inp[5:5+n_alien])
    n_queries = int(inp[5+n_alien])
    queries = list(map(lambda q: tuple(intList(q.split())),
                       inp[6+n_alien:6+n_alien+n_queries]))
    return (start, commands, speed, aliens, queries)
