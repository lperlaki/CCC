import numpy as np
import parser
from util import write


def walk(point, directions, speed, start_tick, end_ticks=1):
    direction = 0
    points = [point.copy()]
    tick = start_tick

    for command, steps in directions:
        if command == 'T':
            direction = (direction + steps) % 4
        elif command == 'F':
            for _ in range(steps):
                if tick > end_ticks - 1/speed:
                    return (points, point)
                tick += 1/speed
                if direction == 0:
                    point.x += 1
                elif direction == 1:
                    point.y += 1
                elif direction == 2:
                    point.x -= 1
                elif direction == 3:
                    point.y -= 1
                points.append(point.copy())
    return (points, point)


def list_queries(start, directions, speed, aliens, queries):
    r = []
    for query in queries:
        time = query[0]
        alien_id = query[1]
        alien_start_tick = aliens[alien_id]
        _, (x, y) = walk(start.copy(), directions, speed, alien_start_tick, time)
        r.append(f'{time} {alien_id} {x} {y}')
    return r


def main():
    for i in range(0, 6):
        write(3, i, '\n'.join(list_queries(*parser.lvl3(i))))


if __name__ == "__main__":
    main()
