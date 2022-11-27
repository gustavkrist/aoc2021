import sys
import networkx as nx
from functools import lru_cache
import pprint
pprint = pprint.pprint


def read_input(f):
    board = f.read().split('\n')
    board[3] += '  '
    board[4] += '  '
    board = tuple((tuple(row) for row in board))
    return board


def valid_moves(board):
    moves = []
    columns = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
    point_dict = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
    for i, let in zip(columns.values(), columns.keys()):
        if board[3][i] not in [let, '.']:
            if board[2][i] == '.':
                cl = board[3][i]
                for j in range(i, 0, -1):
                    if j not in columns.values():
                        if board[1][j] == '.':
                            points = (2 + (i-j)) * point_dict[cl]
                            moves.append(((3, i), (1, j)))
                        else:
                            break
                for j in range(i, 12):
                    if j not in columns.values():
                        if board[1][j] == '.':
                            points = (2 + (j-i)) * point_dict[cl]
                            moves.append(((3, i), (1, j)))
                        else:
                            break
                obstructed = False
                if i > columns[cl]:
                    for j in range(columns[cl], i):
                        if board[1][j] != '.':
                            obstructed = True
                else:
                    for j in range(i+1, columns[cl]+1):
                        if board[1][j] != '.':
                            obstructed = True
                if not obstructed:
                    if board[3][columns[cl]] == '.':
                        if i > columns[cl]:
                            points = (2 + (i-j) + 2) * point_dict[cl]
                        else:
                            points = (2 + (j-i) + 2) * point_dict[cl]
                        moves.append(((3, i), (3, columns[cl])))
                    elif board[3][columns[cl]] == cl and board[2][columns[cl]] == '.':
                        if i > columns[cl]:
                            points = (2 + (i-j) + 1) * point_dict[cl]
                        else:
                            points = (2 + (j-i) + 1) * point_dict[cl]
                        moves.append(((3, i), (2, columns[cl])))
            elif board[2][i] != '.':
                cl = board[2][i]
                for j in range(i, 0, -1):
                    if j not in columns.values():
                        if board[1][j] == '.':
                            points = (1 + (i-j)) * point_dict[cl]
                            moves.append(((2, i), (1, j)))
                        else:
                            break
                for j in range(i, 12):
                    if j not in columns.values():
                        if board[1][j] == '.':
                            points = (1 + (j - i)) * point_dict[cl]
                            moves.append(((2, i), (1, j)))
                        else:
                            break
                obstructed = False
                if i > columns[cl]:
                    for j in range(columns[cl], i):
                        if board[1][j] != '.':
                            obstructed = True
                else:
                    for j in range(i+1, columns[cl]+1):
                        if board[1][j] != '.':
                            obstructed = True
                if not obstructed:
                    if board[3][columns[cl]] == '.':
                        if i > columns[cl]:
                            points = (1 + (i-j) + 2) * point_dict[cl]
                        else:
                            points = (1 + (j-i) + 2) * point_dict[cl]
                        moves.append(((2, i), (3, columns[cl])))
                    elif board[3][columns[cl]] == cl and board[2][columns[cl]] == '.':
                        if i > columns[cl]:
                            points = (1 + (i-j) + 1) * point_dict[cl]
                        else:
                            points = (1 + (j-i) + 1) * point_dict[cl]
                        moves.append(((2, i), (2, columns[cl])))
        else:
            if board[2][i] not in [let, '.']:
                cl = board[2][i]
                for j in range(i, 0, -1):
                    if j not in columns.values():
                        if board[1][j] == '.':
                            points = (1 + (i-j)) * point_dict[cl]
                            moves.append(((2, i), (1, j)))
                        else:
                            break
                for j in range(i, 12):
                    if j not in columns.values():
                        if board[1][j] == '.':
                            points = (1 + (j - i)) * point_dict[cl]
                            moves.append(((2, i), (1, j)))
                        else:
                            break
                obstructed = False
                if i > columns[cl]:
                    for j in range(columns[cl], i):
                        if board[1][j] != '.':
                            obstructed = True
                else:
                    for j in range(i+1, columns[cl]+1):
                        if board[1][j] != '.':
                            obstructed = True
                if not obstructed:
                    if board[3][columns[cl]] == '.':
                        if i > columns[cl]:
                            points = (1 + (i-j) + 2) * point_dict[cl]
                        else:
                            points = (1 + (j-i) + 2) * point_dict[cl]
                        moves.append(((2, i), (3, columns[cl])))
                    elif board[3][columns[cl]] == cl and board[2][columns[cl]] == '.':
                        if i > columns[cl]:
                            points = (1 + (i-j) + 1) * point_dict[cl]
                        else:
                            points = (1 + (j-i) + 1) * point_dict[cl]
                        moves.append(((2, i), (2, columns[cl])))
    for i in range(1, 12):
        if board[1][i] != '.':
            let = board[1][i]
            obstructed = False
            if i > columns[let]:
                for j in range(columns[let], i):
                    if board[1][j] != '.':
                        obstructed = True
            else:
                for j in range(i+1, columns[let]+1):
                    if board[1][j] != '.':
                        obstructed = True
            if not obstructed:
                if board[3][columns[let]] == '.':
                    if i > columns[let]:
                        points = ((i-columns[let]) + 2) * point_dict[let]
                    else:
                        points = ((columns[let]-i) + 2) * point_dict[let]
                    moves.append(((1, i), (3, columns[let])))
                elif board[3][columns[let]] == let and board[2][columns[let]] == '.':
                    if i > columns[let]:
                        points = ((i-columns[let]) + 1) * point_dict[let]
                    else:
                        points = ((columns[let]-i) + 1) * point_dict[let]
                    moves.append(((1, i), (2, columns[let])))
    return moves


def can_move(board, row, col):
    columns = {3: 'A', 5: 'B', 7: 'C', 9: 'D'}
    done = True
    for i in range(5, 1, -1):
        if board[i][col] not in [columns[col], '.']:
            done = False
    if not done:
        can = True
        for i in range(2, row):
            if board[i][col] != '.':
                can = False
    else:
        can = False
    return can


def row1_moves(board, row, col):
    illegal = [3, 5, 7, 9]
    possible = []
    for j in range(col-1, 0, -1):
        if j not in illegal:
            if board[1][j] == '.':
                possible.append(j)
            else:
                break
    for j in range(col+1, 12):
        if j not in illegal:
            if board[1][j] == '.':
                possible.append(j)
            else:
                break
    return possible


def homecol_possible(board, row, col, row1pos=[]):
    if not row1pos:
        row1pos = row1_moves(board, row, col)
    columns = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
    let = board[row][col]
    hc = columns[let]
    allowed = True
    for i in range(5, 1, -1):
        if board[i][hc] not in [let, '.']:
            allowed = False
            break
    if allowed:
        if hc > col:
            if hc-1 not in row1pos and hc-1 != col:
                allowed = False
        elif hc < col:
            if hc+1 not in row1pos and hc+1 != col:
                allowed = False
    if allowed:
        hcrow = None
        for i in range(5, 1, -1):
            if board[i][hc] == '.':
                hcrow = i
                break
    else:
        hcrow = None
    return (hcrow, hc) if hcrow else None


def part2_moves(board):
    moves = []
    columns = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
    for col in columns.values():
        for row in range(5, 1, -1):
            if board[row][col] != '.':
                if can_move(board, row, col):
                    row1 = row1_moves(board, row, col)
                    for c in row1:
                        moves.append(((row, col), (1, c)))
                    hc = homecol_possible(board, row, col, row1)
                    if hc:
                        moves.append(((row, col), hc))
    for col in range(1, 12):
        if board[1][col] != '.':
            hc = homecol_possible(board, 1, col)
            if hc:
                moves.append(((1, col), hc))
    return moves


def finished(board):
    columns = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
    fin = True
    for k, v in columns.items():
        if not (board[2][v] == k and board[3][v] == k and board[4][v] == k and board[5][v] == k):
            fin = False
    return fin


def do_move(board, move):
    (i1, j1), (i2, j2) = move
    let = board[i1][j1]
    lboard = [list(row) for row in board]
    lboard[i1][j1] = '.'
    lboard[i2][j2] = let
    return tuple((tuple(row) for row in lboard)), let


def isstate(board, points):
    state = (('#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'),
             ('#', '.', 'A', '.', '.', '.', 'C', '.', 'D', '.', '.', '.', '#'),
             ('#', '#', '#', '.', '#', '.', '#', 'A', '#', 'C', '#', '#', '#'),
             (' ', ' ', '#', '.', '#', 'D', '#', 'B', '#', 'B', '#', ' ', ' '),
             (' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' '))
    if board == state:
        return True


@lru_cache(maxsize=None)
def sim(board, depth=0):
    moves = part2_moves(board)
    if moves:
        for move in moves:
            p1, p2 = move
            new_board, let = do_move(board, (p1, p2))
            added_points = price(p1, p2, let)
            G.add_edge(board, new_board, weight=added_points)
            sim(new_board, depth+1)
    else:
        ended_states.append((depth, board))
    #     pprint(board)
    # if finished(board):
        # print(board)


def price(p1, p2, let):
    point_dict = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
    points = p2[0] - (2 - p1[0]) + abs(p1[1]-p2[1])
    # if p1[0] == 1:
    #     points = p2[0] - 1 + abs(p1[1]-p2[1])
    # elif p1[0] == 2:
    #     points = p2[0] + abs(p1[1]-p2[1])
    # else:
    #     points = p2[0] + 1 + abs(p1[1]-p2[1])
    return points * point_dict[let]


ended_states = []
# board = read_input(sys.stdin)
# pprint(board)
# board = (('#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'),
#          ('#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'),
#          ('#', '#', '#', 'A', '#', 'D', '#', 'A', '#', 'C', '#', '#', '#'),
#          (' ', ' ', '#', 'D', '#', 'C', '#', 'B', '#', 'A', '#', ' ', ' '),
#          (' ', ' ', '#', 'D', '#', 'B', '#', 'A', '#', 'C', '#', ' ', ' '),
#          (' ', ' ', '#', 'C', '#', 'D', '#', 'B', '#', 'B', '#', ' ', ' '),
#          (' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' '))
board = (('#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'),
         ('#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'),
         ('#', '#', '#', 'B', '#', 'C', '#', 'B', '#', 'D', '#', '#', '#'),
         (' ', ' ', '#', 'D', '#', 'C', '#', 'B', '#', 'A', '#', ' ', ' '),
         (' ', ' ', '#', 'D', '#', 'B', '#', 'A', '#', 'C', '#', ' ', ' '),
         (' ', ' ', '#', 'A', '#', 'D', '#', 'C', '#', 'A', '#', ' ', ' '),
         (' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' '))
state = (('#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'),
         ('#', 'B', 'B', '.', 'D', '.', 'B', '.', 'C', '.', 'D', 'D', '#'),
         ('#', '#', '#', '.', '#', '.', '#', '.', '#', 'C', '#', '#', '#'),
         (' ', ' ', '#', 'A', '#', '.', '#', '.', '#', 'A', '#', ' ', ' '),
         (' ', ' ', '#', 'A', '#', '.', '#', '.', '#', 'C', '#', ' ', ' '),
         (' ', ' ', '#', 'A', '#', 'D', '#', 'C', '#', 'B', '#', ' ', ' '),
         (' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' '))
G = nx.DiGraph()
sim(board)
fin = (('#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'),
       ('#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'),
       ('#', '#', '#', 'A', '#', 'B', '#', 'C', '#', 'D', '#', '#', '#'),
       (' ', ' ', '#', 'A', '#', 'B', '#', 'C', '#', 'D', '#', ' ', ' '),
       (' ', ' ', '#', 'A', '#', 'B', '#', 'C', '#', 'D', '#', ' ', ' '),
       (' ', ' ', '#', 'A', '#', 'B', '#', 'C', '#', 'D', '#', ' ', ' '),
       (' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' '))
# fin = (('#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'),
#        ('#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'),
#        ('#', '#', '#', 'A', '#', 'B', '#', 'C', '#', 'D', '#', '#', '#'),
#        (' ', ' ', '#', 'A', '#', 'B', '#', 'C', '#', 'D', '#', ' ', ' '),
#        (' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' '))
# pprint(list(G.nodes))
length, path = nx.single_source_dijkstra(G, board, target=fin, weight='weight')
print(length)
# for i, state in enumerate(path):
#     print(i)
#     pprint(state)
# print(eval('[' + str(sim(board)).replace('[','').replace(']','') + ']'))
# pprint(ended_boards)
# pprint(state)
# pprint(part2_moves(state))
# pprint(sorted(ended_states, key=lambda x: x[0]))
