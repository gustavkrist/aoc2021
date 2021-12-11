from collections import Counter
import pprint
pprint = pprint.pprint


def star1(data):
    points = []
    for x1, y1, x2, y2 in data:
        if x1 == x2:
            points.extend([(x1, y) for y in (range(y1, y2+1) if y1<y2 else range(y2, y1+1))])
        elif y1 == y2:
            points.extend([(x, y1) for x in (range(x1, x2+1) if x1<x2 else range(x2, x1+1))])
    occurences = Counter(points)
    print(len([(point, count) for (point, count) in occurences.items() if count > 1]))


def star2(data):
    points = []
    for x1, y1, x2, y2 in data:
        if x1 == x2:
            points.extend([(x1, y) for y in (range(y1, y2+1) if y1<y2 else range(y2, y1+1))])
        elif y1 == y2:
            points.extend([(x, y1) for x in (range(x1, x2+1) if x1<x2 else range(x2, x1+1))])
        else:
            a = round((y2-y1) / (x2-x1))
            b = y2 - a*x2
            points.extend([(x, round(a*x+b)) for x in (range(x1, x2+1) if x1<x2 else range(x2, x1+1))])
    occurences = Counter(points)
    print(len([(point. count) for (point, count) in occurences.items() if count > 1]))


def main():
    with open("input.txt") as f:
        data = []
        for line in f:
            coords = line.rstrip().split(' -> ')
            x1, y1 = coords[0].split(',')
            x2, y2 = coords[1].split(',')
            data.append([int(x1), int(y1), int(x2), int(y2)])
    star1(data)
    print()
    star2(data)


if __name__ == "__main__":
    main()
