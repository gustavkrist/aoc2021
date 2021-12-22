import sys
import numpy as np


def read_input(f):
    ranges = []
    for line in f:
        op, xyz = line.rstrip().split(' ')
        xyz = xyz.split(',')
        xyz = list(map(lambda x: tuple(x[2:].split('..')), xyz))
        x, y, z = list(map(lambda x: (int(x[0])+50, int(x[1])+50), xyz))
        ranges.append([op, x, y, z])
    return ranges


def op(eng, range):
    op, (x1, x2), (y1, y2), (z1, z2) = range
    in_range = list(map(lambda x: 0 <= x <= 100, [x1, x2, y1, y2, z1, z2]))
    op = 0 if op == 'off' else 1
    if sum(in_range) == 6:
        eng[x1:x2+1, y1:y2+1, z1:z2+1] = op
    return eng


def main():
    ranges = read_input(sys.stdin)
    eng = np.zeros((101, 101, 101), int)
    for range in ranges:
        eng = op(eng, range)
    uni, counts = np.unique(eng, return_counts=True)
    print(int(counts[np.where(uni == 1)]))


if __name__ == '__main__':
    main()
