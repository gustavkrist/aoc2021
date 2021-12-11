import numpy as np
import pprint
pprint = pprint.pprint


def star1(nums, boards):
    boards_marked = [np.array([["" for i in range(5)] for l in range(5)], dtype='object') for j in range(len(boards))]
    winner = None
    for num in nums:
        if winner:
            break
        for i, board in enumerate(boards):
            if num in board:
                row, col = np.where(board == num)
                boards_marked[i][row, col] += "*"
                if not '' in boards_marked[i][row] or not '' in boards_marked[i][:, col]:
                    winner = i
                    winnum = num
                    mask = boards_marked[i] == ''
                    break
    print(boards[winner])
    print(boards_marked[winner])
    print(sum(boards[winner][mask]) * winnum)


def star2(nums, boards):
    boards_marked = [np.array([["" for i in range(5)] for l in range(5)], dtype='object') for j in range(len(boards))]
    winner = None
    wincount = 0
    for num in nums:
        if winner:
            break
        for i, board in enumerate(boards):
            if num in board:
                row, col = np.where(board == num)
                if boards_marked[i][0, 0] == 'won':
                    pass
                else:
                    boards_marked[i][row, col] += "*"
                    if not '' in boards_marked[i][row] or not '' in boards_marked[i][:, col]:
                        if (wincount + 1) < len(boards):
                            boards_marked[i][0, 0] = 'won'
                            wincount += 1
                        else:
                            winner = i
                            winnum = num
                            mask = boards_marked[i] == ''
                            break
    pprint(boards_marked)
    print(boards[winner])
    print(boards_marked[winner])
    print(sum(boards[winner][mask]) * winnum)


def main():
    with open("input.txt") as f:
        nums = [int(v) for v in f.readline().rstrip().split(',')]
        boards = []
        while f.readline():
            boards.append(np.array([f.readline().rstrip().split() for i in range(5)], dtype=int))
    star1(nums, boards)
    print()
    star2(nums, boards)


if __name__ == "__main__":
    main()
