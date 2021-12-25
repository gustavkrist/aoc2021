import sys
import numpy as np
from functools import lru_cache


def read_input(f):
    return np.array([list(line.rstrip()) for line in f])


@lru_cache(maxsize=None)
def mod(x, m):
    return x % m


def move(arr):
    changed = False
    mr, mc = arr.shape
    staged = []
    for i, row in enumerate(arr):
        for j, tile in enumerate(row):
            if tile == '>':
                next = mod(j+1, mc)
                if arr[i, next] == '.':
                    staged.append(((i, j), (i, next)))
    for p1, p2 in staged:
        arr[p1] = '.'
        arr[p2] = '>'
    if staged:
        changed = True
    staged.clear()
    for i, row in enumerate(arr):
        for j, tile in enumerate(row):
            if tile == 'v':
                next = mod(i+1, mr)
                if arr[next, j] == '.':
                    staged.append(((i, j), (next, j)))
    for p1, p2 in staged:
        arr[p1] = '.'
        arr[p2] = 'v'
    if staged:
        changed = True
    return arr, changed


arr = read_input(sys.stdin)
print(arr)
i = 0
while True:
    arr, changed = move(arr)
    print()
    print(arr)
    if not changed:
        part1 = i+1
        break
    i += 1
print(part1)
