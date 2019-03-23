import numpy as np
import parser
from util import write


def walk(point, directions):
    direction = 0
    points = [point.copy()]
    for command, steps in directions:
        if command == 'T':
            direction = (direction + steps) % 4
        elif command == 'F':
            for _ in range(steps):
                if direction == 0:
                    point.x += 1
                elif direction == 1:
                    point.y += 1
                elif direction == 2:
                    point.x -= 1
                elif direction == 3:
                    point.y -= 1
                points.append(point.copy())
    return points


def main():
    for i in range(1, 6):
        write(2, i, '\n'.join(list(map(str, walk(*parser.lvl2(i))))))


if __name__ == "__main__":
    main()
