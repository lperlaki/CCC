def read(level, nr):
    with open(f'level{level}/level{level}_{nr}.in') as f:
        return f.readlines()


def write(level, nr, s):
    with open(f'level{level}/level{level}_{nr}.out', 'w') as f:
        f.write(s)
