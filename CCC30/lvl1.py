import numpy as np
import parser
from util import write


def walk(point, directions):
    direction = 0
    for command, steps in directions:
        if command == 'T':
            direction = (direction + steps) % 4
        elif command == 'F':
            if direction == 0:
                point.x += steps
            elif direction == 1:
                point.y += steps
            elif direction == 2:
                point.x -= steps
            elif direction == 3:
                point.y -= steps
    return point


def main():
    for i in range(1, 6):
        write(1, i, str(walk(*parser.lvl1(i))))


if __name__ == "__main__":
    main()
