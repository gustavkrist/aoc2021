import sys
from time import perf_counter


def isplane(range):
    xr, yr, zr = range
    if (xr[0] > xr[1] or yr[0] > yr[1] or zr[0] > zr[1]):
        return True


class Cuboid:
    def __init__(self, p1, p2, state):
        xr, yr, zr = (p1[0], p2[0]), (p1[1], p2[1]), (p1[2], p2[2])
        self.ranges = [(xr, yr, zr)]
        self.on = (xr[1]-xr[0]+1)*(yr[1]-yr[0]+1)*(zr[1]-zr[0]+1) if state == 'on' else 0
        self.state = state

    def __mul__(self, other):
        (a1, a2), (b1, b2), (c1, c2) = other.ranges[0]
        new_ranges = []
        for ran in self.ranges:
            (x1, x2), (y1, y2), (z1, z2) = ran
            if not ((x2 < a1 or a2 < x1) or (y2 < b1 or b2 < y1)
                    or (z2 < c1 or c2 < z1)):

                # Checking X
                if a1 <= x1 and a2 <= x2:
                    xr = (x1, a2)
                elif x1 <= a1 and x2 <= a2:
                    xr = (a1, x2)
                elif a1 <= x1 and x2 <= a2:
                    xr = (x1, x2)
                else:
                    xr = (a1, a2)

                # Checking Y
                if b1 <= y1 and b2 <= y2:
                    yr = (y1, b2)
                elif y1 <= b1 and y2 <= b2:
                    yr = (b1, y2)
                elif b1 <= y1 and y2 <= b2:
                    yr = (y1, y2)
                else:
                    yr = (b1, b2)

                # Checking Z
                if c1 <= z1 and c2 <= z2:
                    zr = (z1, c2)
                elif z1 <= c1 and z2 <= c2:
                    zr = (c1, z2)
                elif c1 <= z1 and z2 <= c2:
                    zr = (z1, z2)
                else:
                    zr = (c1, c2)

                area = (xr[1]-xr[0]+1)*(yr[1]-yr[0]+1)*(zr[1]-zr[0]+1)
                self.on -= area
                r1 = ((x1, x2), (y1, yr[0]-1), (z1, z2))
                if not isplane(r1):
                    new_ranges.append(r1)
                r2 = ((x1, x2), (yr[1]+1, y2), (z1, z2))
                if not isplane(r2):
                    new_ranges.append(r2)
                r3 = ((x1, x2), yr, (z1, zr[0]-1))
                if not isplane(r3):
                    new_ranges.append(r3)
                r4 = ((x1, x2), yr, (zr[1]+1, z2))
                if not isplane(r4):
                    new_ranges.append(r4)
                r5 = ((x1, xr[0]-1), yr, zr)
                if not isplane(r5):
                    new_ranges.append(r5)
                r6 = ((xr[1]+1, x2), yr, zr)
                if not isplane(r6):
                    new_ranges.append(r6)
            else:
                new_ranges.append(ran)
        self.ranges = new_ranges

    def __int__(self):
        return self.on


start = perf_counter()
cubes = []
lines = sys.stdin.read().split('\n')
for line in lines:
    state, points = line.rstrip().split(' ')
    points = points.split(',')
    (x1, x2), (y1, y2), (z1, z2) = list(map(lambda x: tuple(map(int, x[2:].split('..'))), points))
    cube = Cuboid((x1, y1, z1), (x2, y2, z2), state)
    for c1 in cubes:
        c1 * cube
    if cube.state == 'on':
        cubes.append(cube)
print(sum(list(map(int, cubes))))
end = perf_counter()
print(end-start)
