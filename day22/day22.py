import sys
import numpy as np
from itertools import chain


def read_input(f):
    ranges = []
    for line in f:
        op, xyz = line.rstrip().split(' ')
        xyz = xyz.split(',')
        xyz = list(map(lambda x: tuple(x[2:].split('..')), xyz))
        x, y, z = list(map(lambda x: (int(x[0])+50, int(x[1])+50), xyz))
        ranges.append([op, x, y, z])
    mac = max(list(map(lambda x: max(x), list(
        map(lambda x: list(chain(*x[1:])), ranges)))))
    mic = min(list(map(lambda x: min(x), list(
        map(lambda x: list(chain(*x[1:])), ranges)))))
    return ranges, mic, mac


def op(eng, range):
    op, (x1, x2), (y1, y2), (z1, z2) = range
    in_range = list(map(lambda x: 0 <= x <= 100, [x1, x2, y1, y2, z1, z2]))
    op = 0 if op == 'off' else 1
    if sum(in_range) == 6:
        eng[x1:x2+1, y1:y2+1, z1:z2+1] = op
    return eng


# def intersection(r1, r2):
#     o1, (x11, x12), (y11, y12), (z11, z12) = r1
#     o2, (x21, x22), (y21, y22), (z21, z22) = r2
#     new_ranges = []
#     if not (x21 <= x22 <= x11 or x12 <= x21 <= x22):
#         if x21 <= x11 and x12 <= x22:
#             pass
#         elif x11


def main():
    ranges, mic, mac = read_input(sys.stdin)
    eng = np.zeros((101, 101, 101), int)
    for range in ranges:
        eng = op(eng, range)
    uni, counts = np.unique(eng, return_counts=True)
    print(int(counts[np.where(uni == 1)]))
    print(mac-mic)


if __name__ == '__main__':
    main()
