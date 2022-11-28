import sys
import networkx as nx
import pprint
pprint = pprint.pprint


def generate_graph(data):
    G = nx.Graph()
    for edge in data:
        node1, node2 = edge.split('-')
        G.add_edge(node1, node2)
    for node in G.nodes:
        if node not in ['start', 'end']:
            if 65 <= ord(node[0]) <= 90:
                G.nodes[node]['size'] = 'big'
            else:
                G.nodes[node]['size'] = 'small'
        else:
            G.nodes[node]['size'] = None
    return G


def size(G, node):
    return G.nodes[node]['size']


def dfs(G, node, visited, path, paths, part2, twice=False):
    if node == 'end':
        paths.append(path + [node])
        return
    if size(G, node) == 'small':
        visited[node] += 1
        if visited[node] > 1 and part2:
            twice = True
    for neighbor in G[node]:
        if visited[neighbor] > 0 and not twice and part2 and neighbor != 'start':
            paths.append(path + [node])
            dfs(G, neighbor, visited, path + [node], paths, part2, twice)
        elif visited[neighbor] < 1 and neighbor != 'start':
            paths.append(path + [node])
            dfs(G, neighbor, visited, path + [node], paths, part2, twice)
    visited[node] -= 1
    twice = False


def find_paths(G, part2=False):
    visited = {node: 0 for node in G.nodes}
    path = []
    paths = []
    dfs(G, 'start', visited, path, paths, part2)
    start_end_paths = [p for p in paths if p[-1] == 'end']
    return len(start_end_paths)


def main():
    data = list(map(str.rstrip, sys.stdin.readlines()))
    G = generate_graph(data)
    result = []
    with open('result.txt') as f:
        for line in f:
            result.append(tuple(line.rstrip().split(',')))
    print(find_paths(G))
    print(find_paths(G, part2=True))


if __name__ == "__main__":
    main()
