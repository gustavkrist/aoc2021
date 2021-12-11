def fish_growth(data, days):
    # fish = data.copy()
    # for i in range(days):
    #     new_fish = []
    #     for j in range(len(fish)):
    #         fish[j] -= 1
    #         if fish[j] < 0:
    #             fish[j] = 6
    #             new_fish.append(8)
    #     fish.extend(new_fish)
    # print(len(fish))
    fish = {i: 0 for i in range(9)}
    for i in data:
        fish[i] += 1

    for day in range(days):
        zeros = fish[0]
        for i in range(1, 9):
            fish[i-1] = fish[i]
        fish[8] = zeros
        fish[6] += zeros
    print(sum(list(fish.values())))


def main():
    with open("input.txt") as f:
        data = [int(i) for i in f.readline().rstrip().split(',')]
    fish_growth(data, 80)
    print()
    fish_growth(data, 256)


if __name__ == "__main__":
    main()
