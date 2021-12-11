import math


def fuel(data):
    low = min(data)
    high = max(data)
    lowest = math.inf
    for i in range(low, high + 1):
        total_fuel = 0
        for crab in data:
            total_fuel += abs(crab-i)
        if total_fuel < lowest:
            lowest = total_fuel
    print(lowest)


def fuel2(data):
    low = min(data)
    high = max(data)
    lowest = math.inf
    for i in range(low, high + 1):
        total_fuel = 0
        for crab in data:
            n = abs(crab-i)
            total_fuel += round((n*(n+1)) / 2)
        if total_fuel < lowest:
            lowest = total_fuel
    print(lowest)


def main():
    with open("input.txt") as f:
        data = [int(i) for i in f.readline().rstrip().split(",")]
    fuel(data)
    print()
    fuel2(data)


if __name__ == '__main__':
    main()
