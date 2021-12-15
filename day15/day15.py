import sys
import networkx as nx
import numpy as np


def read_input(input):
    data = []
    for line in input:
        data.append(list(map(int, line.rstrip())))
    rows, cols = len(data[0]), len(data)
    return data, rows, cols


def generate_graph(data):
    G = nx.Graph()
    for i, row in enumerate(data):
        for j, n in enumerate(row):
            G.add_node((i, j), weight=n)
    rows, cols = len(data)-1, len(data[0])-1
    for i, j in G.nodes:
        for di, dj in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            if 0 <= i+di <= rows and 0 <= j+dj <= cols:
                u, v = (i, j), (i+di, j+dj)
                G.add_edge(u, v)
    return G


def expand_row(arr, i=1):
    if i >= 4:
        return np.c_[arr, arr % 9 + 1]
    return np.c_[arr, expand_row(arr % 9 + 1, i+1)]


def expand_map(data):
    arr = np.array(data)
    new_arr = expand_row(arr)
    for i in range(1, 5):
        new_arr = np.r_[new_arr, expand_row(arr % 9 + i)]
    return new_arr


def lowest_path(G, source, end):
    return nx.dijkstra_path_length(G, source, end, weight=lambda u, v, d: G.nodes[v]['weight'])


def main():
    data, rows, cols = read_input(sys.stdin)
    full_map = expand_map(data)
    G = generate_graph(full_map)
    print(lowest_path(G, (0, 0), (rows-1, cols-1)))
    print(lowest_path(G, (0, 0), (rows*5-1, cols*5-1)))


if __name__ == '__main__':
    main()
