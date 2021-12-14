import sys
from collections import Counter
import itertools


def create_pair_dict(file):
    sys.stdin.readline()
    pair_dict = {}
    for line in file:
        k, v = line.rstrip().split(' -> ')
        pair_dict[k] = v
    return pair_dict


def pair_insertion(chain, pair_dict, depth=0):
    if depth >= 40:
        return chain[:-1]
    new_chain = []
    for p1, p2 in zip(chain, chain[1:]):
        if depth < 5:
            print(depth, p1 + p2)
        new_chain += pair_insertion([p1, pair_dict[p1+p2], p2], pair_dict, depth+1)
    return new_chain


def star1(chain):
    counts = Counter(chain)
    most = max(counts, key=lambda x: counts[x])
    least = min(counts, key=lambda x: counts[x])
    return counts[most] - counts[least]


def main():
    chain = list(sys.stdin.readline().rstrip())
    pair_dict = create_pair_dict(sys.stdin)
    for i in range(1):
        new_chain = pair_insertion(chain, pair_dict)
        new_chain.append(chain[-1])
        chain = new_chain
    print(star1(chain))


if __name__ == '__main__':
    main()
