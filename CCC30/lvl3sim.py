import numpy as np
import parser
from util import write
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


class Alien:
    def __init__(self, start=Point(), speed=1, spawn_tick=0):
        self.speed = speed
        self.spawn_tick = spawn_tick
        self.start = start

    def simulate(self, directions, ticks):
        directions = iter(directions)
        position = self.start.copy()
        ticks -= self.spawn_tick
        amount = 0
        direction = 0
        command, steps = next(directions)
        for tick in range(ticks):
            amount += self.speed
            while amount >= 1:
                if steps <= 0:
                    command, steps = next(directions)
                if command == 'T':
                    direction = (direction + steps) % 4
                    steps = 0
                    continue
                elif command == 'F':
                    if direction == 0:
                        position.x += 1
                    elif direction == 1:
                        position.y += 1
                    elif direction == 2:
                        position.x -= 1
                    elif direction == 3:
                        position.y -= 1
                    steps -= 1
                    amount -= 1
        return position

    def compute(self, directions, ticks):
        return self.start + sum(directions[:int((ticks - self.spawn_tick)*self.speed)])


def list_queries(start, directions, speed, aliens, queries):
    r = []
    computed_directions = computePath(directions)
    aliens = list(map(lambda spawn_tick: Alien(
        start.copy(), directions, speed, spawn_tick), aliens))
    for query in queries:
        time = query[0]
        alien_id = query[1]
        alien = aliens[alien_id]
        # x, y = alien.simulate(directions, time)
        x, y = alien.compute(computed_directions, time)
        r.append(f'{time} {alien_id} {x} {y}')
    return r


def main():
    for i in range(1, 6):
        write(3, i, '\n'.join(list_queries(*parser.lvl3(i))))


if __name__ == "__main__":
    main()
