def star1():
    count = 0
    summ = 0
    with open("input.txt") as infile:
        prev = int(infile.readline())
        for line in infile:
            if int(line) > prev:
                count += 1
            prev = int(line)
    print(count)


# def star2():
#     count = 0
#     with open("input.txt") as infile:
#         sliding = []
#         for line in infile:
#             sliding.append([])
#             for i in range(len(sliding)):
#                 if len(sliding[i]) < 3:
#                     sliding[i].append(int(line))
#         sliding_values = [sum(l) for l in sliding if len(l) == 3]
#         prev = sliding_values[0]
#         for v in sliding_values[1:]:
#             if v >= prev:
#                 count += 1
#                 prev = v
#     print(count)


def star2(data):
    increasing = sum([1 for d1, d2, d3, d4 in zip(data, data[1:], data[2:], data[3:]) if sum([d1, d2, d3]) < sum([d2, d3, d4])])
    print(increasing)


def main():
    with open("input.txt") as infile:
        data = [int(line) for line in infile]
    part1 = sum([1 for d1, d2 in zip(data, data[1:]) if d2 > d1])
    print(part1)
    print()
    star2(data)


if __name__ == "__main__":
    main()
