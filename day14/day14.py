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


def pair_insertion(chain, pair_dict):
    # new_chain = [p1 + pair_dict[p1+p2] for p1, p2 in zip(chain, chain[1:])] + [chain[-1]]
    # new_chain = list(itertools.chain(*new_chain))
    n = 1
    new_chains = [[] for i in range(n)]
    for (i, p1), (j, p2) in zip(enumerate(chain), enumerate(chain[1:])):
        new_chains[0] += p1 + pair_dict[]
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
        print(i)
        chain = pair_insertion(chain, pair_dict)
    print(star1(chain))


if __name__ == '__main__':
    main()
