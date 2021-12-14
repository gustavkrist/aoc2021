import sys
import networkx as nx


def readfile(file):
    data = []
    for line in file:
        data.append([int(n) for n in line.rstrip()])
    return data


def create_graph(data):
    edges = []
    G = nx.Graph()
    max_i = len(data) - 1
    max_j = len(data[0]) - 1
    for i, row in enumerate(data):
        for j, n in enumerate(row):
            for di, dj in zip([0,1,1,1,0,-1,-1,-1], [1,1,0,-1,-1,-1,0,1]):
                G.add_node((i, j), energy=n)
                if 0 <= i+di <= max_i and 0 <= j+dj <= max_j:
                    edges.append(((i, j), (i+di, j+dj)))
    G.add_edges_from(edges)
    return G


def flash_stats(G, n):
    flash_total = 0
    octopuses = len(G)
    step = 0
    while True:
        flash_step = 0
        for node in G.nodes:
            G.nodes[node]['energy'] += 1
        incremented = 1
        flashed = set()
        while incremented:
            incremented = 0
            for node in G.nodes:
                if G.nodes[node]['energy'] > 9 and node not in flashed:
                    for neighbor in G[node]:
                        G.nodes[neighbor]['energy'] += 1
                        incremented += 1
                    flashed.add(node)
                    flash_step += 1
        for node in G.nodes:
            if G.nodes[node]['energy'] > 9:
                G.nodes[node]['energy'] = 0
        flash_total += flash_step
        if step == (n-2):
            flashes_n = flash_total
        if flash_step == octopuses:
            first_sync = step + 1
            break
        step += 1
    return flashes_n, first_sync


def main():
    data = readfile(sys.stdin)
    G = create_graph(data)
    flashes, first_sync = flash_stats(G, 100)
    print(flashes)
    print(first_sync)

if __name__ == "__main__":
    main()
