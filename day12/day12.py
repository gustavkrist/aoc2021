import sys
from itertools import chain
import pprint
pprint = pprint.pprint


def create_adj_dict(file):
    adj_dict = {}
    for line in file:
        nodes = line.rstrip().split('-')
        for node1, node2 in zip(nodes, reversed(nodes)):
            if node1 not in adj_dict and node2 != 'start':
                adj_dict[node1] = {node2}
            elif node2 != 'start':
                adj_dict[node1].add(node2)
    return adj_dict


def big(node):
    if len(node) == 1:
        if 65 <= ord(node) <= 90:
            return True
        else:
            return False
    else:
        return False


def find_paths(node, adj_dict, visited):
    pass


def main():
    adj_dict = create_adj_dict(sys.stdin)
    visited = {n: False for n in adj_dict.keys()}
    print(adj_dict)
    adj_dict = {'A': {'c', 'b', 'end'}, 'c': set(), 'b': set()}
    paths = []
    find_paths('A', adj_dict, visited)
    pprint(paths)


if __name__ == "__main__":
    main()
