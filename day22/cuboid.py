import sys
from progressbar import ProgressBar, Bar, Percentage, ETA, FileTransferSpeed
widgets = [Percentage(), ' ', Bar('-'), ' ', ETA(), ' ', FileTransferSpeed()]
pbar = ProgressBar(widgets=widgets)


def ispoint(range):
    xr, yr, zr = range
    if xr[0] == xr[1] and yr[0] == yr[1] and zr[0] == zr[1]:
        return True


class Cuboid:
    def __init__(self, p1, p2, state):
        xr, yr, zr = (p1[0], p2[0]+1), (p1[1], p2[1]+1), (p1[2], p2[2]+1)
        self.ranges = [(xr, yr, zr)]
        self.on = (xr[1]-xr[0])*(yr[1]-yr[0])*(zr[1]-zr[0]) if state == 'on' else 0
        self.turned_off = set()
        # ibar = ProgressBar(widgets=widgets, maxval=(p2[0]-p1[0])*(p2[1]-p1[1])*(p2[2]-p1[2])).start()
        # counter = 0
        # for x in range(p1[0], p2[0]):
        #     for y in range(p1[1], p2[1]):
        #         for z in range(p1[2], p2[2]):
        #             self.on.add((x, y, z))
        #             counter += 1
        #             ibar.update(counter)
        # self.on = set(list(chain(*list(map(lambda x: [(*x, z) for z in range(p1[2], p2[2])],
        #             list(chain(*list(map(lambda x: [(x, y) for y in range(p1[1], p2[1])],
        #                     [x for x in range(p1[0], p2[0])])))))))))

    def __mul__(self, other):
        (a1, a2), (b1, b2), (c1, c2) = other.ranges[0]
        new_ranges = []
        for ran in self.ranges:
            (x1, x2), (y1, y2), (z1, z2) = ran
            if not ((x2 - a1 < 0 or x1 - a2 > 0) or (y2 - b1 < 0 or y1 - b2 > 0)
                    or (z2 - c1 < 0 or z1 - c2 > 0)):

                # Checking X
                if a1 < x1 and a2 < x2:
                    xr = (x1, a2)
                elif x1 < a1 and x2 < a2:
                    xr = (a1, x2)
                elif a1 < x1 and x2 < a2:
                    xr = (x1, x2)
                else:
                    xr = (a1, a2)

                # Checking Y
                if b1 < y1 and b2 < y2:
                    yr = (y1, b2)
                elif y1 < b1 and y2 < b2:
                    yr = (b1, y2)
                elif b1 < y1 and y2 < b2:
                    yr = (y1, y2)
                else:
                    yr = (b1, b2)

                # Checking Z
                if c1 < z1 and c2 < z2:
                    zr = (z1, c2)
                elif z1 < c1 and z2 < c2:
                    zr = (c1, z2)
                elif c1 < z1 and z2 < c2:
                    zr = (z1, z2)
                else:
                    zr = (c1, c2)

                area = (xr[1]-xr[0])*(yr[1]-yr[0])*(zr[1]-zr[0])
                self.on -= area
                print(area)
                r1 = ((x1, xr[0]), (y1, yr[0]), (z1, zr[0]))
                if not ispoint(r1):
                    new_ranges.append(r1)
                r2 = ((xr[1], x2), (yr[1], y2), (zr[1], z2))
                if not ispoint(r2):
                    new_ranges.append(r2)
                print(ran)
                print(other.ranges[0])
                print(xr, yr, zr)
                print(new_ranges)
                print()
        self.ranges = new_ranges

    def __len__(self):
        return self.on

    def __repr__(self):
        return str(self.on)

    def __str__(self):
        return str(self.on)

    def __int__(self):
        return self.on


cubes = []
lines = sys.stdin.read().split('\n')
for line in lines:
    state, points = line.rstrip().split(' ')
    points = points.split(',')
    (x1, x2), (y1, y2), (z1, z2) = list(map(lambda x: tuple(map(int, x[2:].split('..'))), points))
    cube = Cuboid((x1, y1, z1), (x2, y2, z2), state)
    for c1 in cubes:
        c1 * cube
    cubes.append(cube)
print(sum(list(map(int, cubes))))
