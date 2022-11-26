import sys
from functools import lru_cache
from progressbar import ProgressBar, Bar, Percentage, ETA, FileTransferSpeed
widgets = [Percentage(), ' ', Bar('-'), ' ', ETA(), ' ', FileTransferSpeed()]


@lru_cache(maxsize=None)
def xmax(vx):
    return (vx*(vx+1))//2


@lru_cache(maxsize=None)
def xpos(t, vx):
    xp = sum([vx-i for i in range(t)])
    return xp if t <= vx else xmax(vx)


@lru_cache(maxsize=None)
def ymax(vy):
    return (vy*(vy+1))//2 if vy >= 0 else 0


@lru_cache(maxsize=None)
def ypos(t, vy):
    return sum([vy-i for i in range(t)])


@lru_cache(maxsize=None)
def pos(t, vx, vy):
    return (xpos(t, vx), ypos(t, vy))


def main():
    input_line = sys.stdin.readline().rstrip()
    _, xy = input_line.split(': ')
    x, y = xy.split(', ')
    xcoords = list(map(int, x[2:].split('..')))
    ycoords = list(map(int, y[2:].split('..')))
    vx_inbounds = set()
    vx = 0
    while vx <= 67:
        t = 0
        while xpos(t, vx) <= xcoords[1] and t <= vx:
            if xcoords[0] <= xpos(t, vx) <= xcoords[1]:
                vx_inbounds.add(vx)
            t += 1
        vx += 1
    vy_inbounds = set()
    vy = 0
    pbar = ProgressBar(widgets=widgets, maxval=271).start()
    while vy <= 270:
        t = 0
        while t <= 1000:
            if ycoords[0] <= ypos(t, vy) <= ycoords[1] and t <= xpos(t, max(vx_inbounds)):
                vy_inbounds.add(vy)
            t += 1
        vy += 1
        pbar.update(vy)
    vy = 0
    pbar = ProgressBar(widgets=widgets, maxval=261).start()
    while vy >= -260:
        t = 0
        while t <= 1000:
            if ycoords[0] <= ypos(t, vy) <= ycoords[1] and t <= xpos(t, max(vx_inbounds)):
                vy_inbounds.add(vy)
            t += 1
        vy -= 1
        pbar.update(abs(vy))
    vels = set()
    for vx in vx_inbounds:
        for vy in vy_inbounds:
            vels.add((vx, vy))
    for vy in vy_inbounds:
        for vx in vx_inbounds:
            vels.add((vx, vy))
    print()
    print(max(vy_inbounds))
    hits_target = set()
    target_points = set()
    for x in range(xcoords[0], xcoords[1] + 1):
        for y in range(ycoords[0], ycoords[1] + 1):
            target_points.add((x, y))
    for y in range(ycoords[0], ycoords[1] + 1):
        for x in range(xcoords[0], xcoords[1] + 1):
            target_points.add((x, y))
    pbar = ProgressBar(widgets=widgets, maxval=len(vels)+1).start()
    for fdas, (vx, vy) in enumerate(vels):
        t = 0
        while t < 1000:
            if pos(t, vx, vy) in target_points:
                hits_target.add((vx, vy))
            t += 1
        pbar.update(fdas)
    maxy_list = [(vx, vy, ymax(vy)) for vx, vy in hits_target]
    maxy = max(maxy_list, key=lambda x: x[2])
    print()
    print(maxy[2])
    print(len(hits_target))


if __name__ == '__main__':
    main()
