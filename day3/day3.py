import numpy as np


def star1(data):
    common = {i: [0, 0] for i in range(12)}
    for binstr in data:
        for i, val in enumerate(binstr.rstrip()):
            if val == '0':
                common[i][0] += 1
            else:
                common[i][1] += 1
    gamma = ['0' if li[0] > li[1] else '1' for li in common.values()]
    epsilon = ['1' if g == '0' else '0' for g in gamma]
    gamma = ''.join(gamma)
    epsilon = ''.join(epsilon)
    powerdraw = int(gamma, 2) * int(epsilon, 2)
    print(powerdraw)


def star2(data):
    # Oxygen generator value
    i = 0
    arr = np.array([list(le) for le in [li.rstrip() for li in data]])
    while i < 12:
        _, counts = np.unique(arr[:, i], return_counts=True)
        if counts[0] > counts[1]:
            arr = arr[np.where(arr[:, i] == '0')]
        else:
            arr = arr[np.where(arr[:, i] == '1')]
        if arr.shape[0] == 1:
            break
        else:
            i += 1
    oxygen = ''.join(arr[0].tolist())

    i = 0
    arr = np.array([list(le) for le in [li.rstrip() for li in data]])
    while i < 12:
        _, counts = np.unique(arr[:, i], return_counts=True)
        if counts[0] > counts[1]:
            arr = arr[np.where(arr[:, i] == '1')]
        else:
            arr = arr[np.where(arr[:, i] == '0')]
        if arr.shape[0] == 1:
            break
        else:
            i += 1
    co2 = ''.join(arr[0].tolist())

    print(int(oxygen, 2) * int(co2, 2))


def main():
    with open("input.txt") as f:
        data = f.readlines()
    star1(data)
    print()
    star2(data)


if __name__ == "__main__":
    main()
