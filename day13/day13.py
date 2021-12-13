import sys
import pprint
pprint = pprint.pprint


def fold(sheet, coord):
    x_len = len(sheet[0])
    y_len = len(sheet[1])
    fold_axis, fold_coord = coord[11:].split('=')
    fold_coord = int(fold_coord)
    if fold_axis == 'x':
        for i, row in enumerate(sheet):
            for j, dot in enumerate(row[fold_coord+1:]):
                if dot == '#':
                    sheet[i][(fold_coord-1)-j] = '#'
            sheet[i] = sheet[i][:fold_coord]
    else:
        for i, row in enumerate(sheet[fold_coord+1:]):
            for j, dot in enumerate(row):
                if dot == '#':
                    sheet[(fold_coord-1)-i][j] = '#'
        sheet = sheet[:fold_coord]
    return sheet


def parse_file(file):
    points = []
    for line in sys.stdin:
        if line != '\n':
            x, y = map(int, line.rstrip().split(','))
            points.append((x, y))
        else:
            break
    x_len = max(points, key=lambda x: x[0])[0] + 1
    y_len = max(points, key=lambda x: x[1])[1] + 1
    sheet = [['.' for _ in range(x_len)] for _ in range(y_len)]
    for y, x in points:
        sheet[x][y] = '#'
    coords = [line.rstrip() for line in sys.stdin]
    return sheet, coords


def count_dots(sheet):
    dot_count = 0
    for row in sheet:
        for dot in row:
            if dot == '#':
                dot_count += 1
    return dot_count


def main():
    sheet, coords = parse_file(sys.stdin)

    # Part 1
    sheet = fold(sheet, coords[0])
    print(count_dots(sheet))

    # Part 2
    for coord in coords[1:]:
        sheet = fold(sheet, coord)
    for line in sheet:
        print(line)


if __name__ == '__main__':
    main()
