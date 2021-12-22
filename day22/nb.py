import sys
import numpy as np
from numba import njit, prange, int32, int64


def read_input(f):
    ranges = []
    for line in f:
        op, xyz = line.rstrip().split(' ')
        xyz = xyz.split(',')
        xyz = list(map(lambda x: tuple(x[2:].split('..')), xyz))
        x, y, z = list(map(lambda x: (int(x[0]), int(x[1])), xyz))
        ranges.append([op, x, y, z])
    x = list(map(lambda x: x[1], ranges))
    y = list(map(lambda x: x[2], ranges))
    z = list(map(lambda x: x[3], ranges))
    minx = min(x, key=lambda x: x[0])[0]
    miny = min(y, key=lambda x: x[0])[0]
    minz = min(z, key=lambda x: x[0])[0]
    new = list(map(lambda x: (x[0],
                              (x[1][0]-minx, x[1][1]-minx),
                              (x[2][0]-miny, x[2][1]-miny),
                              (x[3][0]-minz, x[3][1]-minz)),
               ranges))
    return new


@njit(int64(int32[:,:]), parallel=True)  # noqa: E231
def lights_on(ranges):
    xs = np.max(ranges[:, 1:3]) + 1
    ys = np.max(ranges[:, 3:5]) + 1
    zs = np.max(ranges[:, 5:]) + 1
    count = 0
    print(zs)
    for z in prange(zs+1):
        print(z)
        arr = np.zeros((xs, ys), dtype='int8')
        for r in ranges:
            if z in np.arange(r[5], r[6]+1):
                for i in range(r[1], r[2]+1):
                    for j in range(r[3], r[4]+1):
                        arr[i, j] = r[0]
                # arr[r[1]:r[2]+1, r[3]:r[4]+1] = r[0]
        count += np.sum(arr)
    return count


def main():
    ranges = read_input(sys.stdin)
    np_ranges = []
    for range in ranges:
        li = [range[0], *range[1], *range[2], *range[3]]
        li[0] = 1 if range[0] == 'on' else 0
        np_ranges.append(li)
    np_ranges = np.array(np_ranges, dtype='int32')
    print(np_ranges)
    print(lights_on(np_ranges))


if __name__ == '__main__':
    main()
