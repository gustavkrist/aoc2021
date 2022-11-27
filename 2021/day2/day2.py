def star1():
    with open("input.txt") as f:
        data = [[s, int(v)] for s, v in [line.split() for line in f]]
    pos = [0, 0]
    for instruc in data:
        if instruc[0] == 'forward':
            pos[0] += instruc[1]
        elif instruc[0] == 'down':
            pos[1] += instruc[1]
        elif instruc[0] == 'up':
            pos[1] -= instruc[1]
    print(pos[0] * pos[1])


def star2():
    with open("input.txt") as f:
        data = [[s, int(v)] for s, v in [line.split() for line in f]]
    pos = [0, 0]
    aim = 0
    for instruc in data:
        if instruc[0] == 'forward':
            pos[0] += instruc[1]
            pos[1] += aim * instruc[1]
        elif instruc[0] == 'down':
            aim += instruc[1]
        elif instruc[0] == 'up':
            aim -= instruc[1]
    print(pos[0] * pos[1])


def main():
    star1()
    print()
    star2()


if __name__ == "__main__":
    main()
