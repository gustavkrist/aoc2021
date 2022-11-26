import sys
from collections import Counter
import itertools
from functools import reduce


def create_pair_dict(file):
    sys.stdin.readline()
    pair_dict = {}
    for line in file:
        k, v = line.rstrip().split(' -> ')
        pair_dict[k] = v
    return pair_dict


def pair_insertion(chain, pair_dict, depth=0):
    if depth >= 10:
        return chain[:-1]
    new_chain = []
    for p1, p2 in zip(chain, chain[1:]):
        new_chain += pair_insertion([p1, pair_dict[p1+p2], p2], pair_dict, depth+1)
    return new_chain


def star1(chain):
    counts = Counter(chain)
    most = max(counts, key=lambda x: counts[x])
    least = min(counts, key=lambda x: counts[x])
    return counts[most] - counts[least]


def star2(chain, pair_dict, n):
    chain_pairs = [p1 + p2 for p1, p2 in zip(chain, chain[1:])]
    pairs = Counter(chain_pairs)
    for i in range(n):
        for (p1, p2), amnt in list(pairs.items()):
            prod = pair_dict[p1+p2]
            pairs[p1+prod] += amnt
            pairs[prod+p2] += amnt
            pairs[p1+p2] -= amnt
    single_count = Counter()
    for (p1, p2), v in pairs.items():
        single_count[p1] += v
        single_count[p2] += v
    single_count[chain[0]] += 1
    single_count[chain[-1]] += 1
    for k in single_count.keys():
        single_count[k] //= 2
    most = max(single_count, key=lambda x: single_count[x])
    # most = reduce(lambda a, b: a if a > b else b, pairs.values())
    least = min(single_count, key=lambda x: single_count[x])
    # least = reduce(lambda a, b: a if a < b and b > 0 else b, single_count.values())
    return single_count[most] - single_count[least]


def main():
    chain = list(sys.stdin.readline().rstrip())
    pair_dict = create_pair_dict(sys.stdin)
    for i in range(1):
        new_chain = pair_insertion(chain, pair_dict)
        new_chain.append(chain[-1])
    print(star1(new_chain))
    print(star2(chain, pair_dict, 40))


if __name__ == '__main__':
    main()
