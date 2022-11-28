import pprint
from collections import Counter
pprint = pprint.pprint


def star(data):
    low_points = []
    low_coords = []
    for row, rowlist in enumerate(data):
        for col, n in enumerate(rowlist):
            if row == 0 and col == 0:
                if rowlist[col+1] > n and data[row+1][col] > n:
                    low_points.append(n)
                    low_coords.append((row, col))
            elif row == 0 and col == (len(rowlist) - 1):
                if rowlist[col-1] > n and data[row+1][col] > n:
                    low_points.append(n)
                    low_coords.append((row, col))
            elif row == (len(data) - 1) and col == 0:
                if rowlist[col+1] > n and data[row-1][col] > n:
                    low_points.append(n)
                    low_coords.append((row, col))
            elif row == (len(data) - 1) and col == (len(rowlist) - 1):
                if rowlist[col-1] > n and data[row-1][col] > n:
                    low_points.append(n)
                    low_coords.append((row, col))
            elif row == 0:
                if rowlist[col-1] > n and rowlist[col+1] > n and data[row+1][col] > n:
                    low_points.append(n)
                    low_coords.append((row, col))
            elif row == (len(data) - 1):
                if rowlist[col-1] > n and rowlist[col+1] > n and data[row-1][col] > n:
                    low_points.append(n)
                    low_coords.append((row, col))
            elif col == 0:
                if rowlist[col+1] > n and data[row-1][col] > n and data[row+1][col] > n:
                    low_points.append(n)
                    low_coords.append((row, col))
            elif col == (len(rowlist) - 1):
                if rowlist[col-1] > n and data[row-1][col] > n and data[row+1][col] > n:
                    low_points.append(n)
                    low_coords.append((row, col))
            else:
                if rowlist[col-1] > n and rowlist[col+1] > n and data[row-1][col] > n and data[row+1][col] > n:
                    low_points.append(n)
                    low_coords.append((row, col))
    total = 0
    for n in low_points:
        total += 1 + n
    print(total)
    return low_coords


def find_basins(data, basins, row, col, enum):
    if not (0 <= row <= (len(data)-1) and 0 <= col <= (len(data[0])-1)):
        return
    elif basins[(row, col)] != 0:
        return
    elif data[row][col] == 9:
        basins[(row, col)] = -1
        return
    else:
        basins[(row, col)] = enum
        find_basins(data, basins, row+1, col, enum)
        find_basins(data, basins, row-1, col, enum)
        find_basins(data, basins, row, col+1, enum)
        find_basins(data, basins, row, col-1, enum)


def main():
    with open("input.txt") as f:
        data = []
        for line in f:
            data.append([int(v) for v in list(line.rstrip())])
    basins = {}
    for row, rowlist in enumerate(data):
        for col, n in enumerate(rowlist):
            basins[(row, col)] = 0
    low_coords = star(data)
    print()
    for enum, coords in enumerate(low_coords):
        row, col = coords
        try:
            find_basins(data, basins, row, col, enum)
        except RecursionError:
            pass
        highest = enum
    print(sum([1 for k, v in basins.items() if v == 0]))
    for k, v in basins.items():
        if v == 0:
            row, col = k
            if data[row][col] == 9:
                basins[k] = -1
            else:
                for r, c in zip([row+1, row-1, row, row], [col, col, col+1, col-1]):
                    if 0 < r < (len(data) - 1) and 0 < c < (len(data[0]) - 1):
                        if basins[(r, c)] != 0 or basins[(r, c)] != -1:
                            basins[k] = basins[(r, c)]
                if basins[k] == 0:
                    basins[k] = highest + 1
                    highest += 1
    print(sum([1 for k, v in basins.items() if v == 0]))
    basin_sizes = Counter([v for v in basins.values() if v > 0])
    top3 = sorted(basin_sizes.values())[-3:]
    print(top3)
    total = top3[0] * top3[1] * top3[2]
    print(total)

if __name__ == "__main__":
    main()
