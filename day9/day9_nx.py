import sys
import networkx as nx
from math import prod


def read_input(input):
    data = []
    for line in input:
        data.append(list(map(int, line.rstrip())))
    return data


def generate_graph(data):
    G = nx.Graph()
    for i, row in enumerate(data):
        for j, n in enumerate(row):
            G.add_node((i,j), weight=n)
    max_i, max_j = [max(G.nodes, key=lambda x: x[i])[i] for i in range(2)]
    for i, j in G.nodes:
        for di, dj in zip([0,0,1,-1], [1,-1,0,0]):
            if 0 <= i+di <= max_i and 0 <= j+dj <= max_j:
                G.add_edge((i,j), (i+di, j+dj))
    return G


def is_lower(G, node):
    for neighbor in G[node]:
        if not G.nodes[node]['weight'] < G.nodes[neighbor]['weight']:
            return False
    return True


def main():
    # Part 1
    G = generate_graph(read_input(sys.stdin))
    low_values = [G.nodes[node]['weight'] for node in G.nodes if is_lower(G, node)]
    print(sum([1 + n for n in low_values]))
    # Part 2
    for node in G.nodes:
        if G.nodes[node]['weight'] == 9:
            G.remove_edges_from([(node, neighbor) for neighbor in G[node]])
    top3 = [len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)][:3]
    print(prod(top3))


if __name__ == '__main__':
    main()
