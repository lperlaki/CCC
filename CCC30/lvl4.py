import parser
import numpy as np
from point import Point


def computePath(directions):
    direction = 0
    path = []
    for command, steps in directions:
        if command == 'T':
            direction = (direction + steps) % 4
        elif command == 'F':
            for _ in range(steps):
                if direction == 0:
                    path.append((1, 0))
                elif direction == 1:
                    path.append((0, 1))
                elif direction == 2:
                    path.append((-1, 0))
                elif direction == 3:
                    path.append((0, -1))
    return np.array(path)


class World:
    def __init__(self, start, path):
        self.path = makePath(path)
        self.start = start


class Alien:
    def __init__(self, start, spawn, path):
        self.pos = start
        self.tick = 0
        self.path = path

    def run(self):
        if self.spawn > self.tick:
            return

        self.tick += 1


class Simulation:
    def __init__(self, aliens, path):
        self.aliens = aliens
        self.path = path

    def tick(self):
        pass


start, directions, speed, aliens, queries = parser.lvl3(1)

w = World(start, directions)

print(list(iter(w.path)))
