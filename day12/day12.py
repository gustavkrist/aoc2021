import networkx as nx


def generate_graph(data):
    G = nx.Graph()
    for edge in data:
        node1, node2 = edge.split('-')
        G.add_edge(node1, node2)
    for node in G.nodes:
        if node not in ['start', 'end']:
            if 65 <= ord(node) <= 90:
                G.nodes[node]['size'] = 'big'
            else:
                G.nodes[node]['size'] = 'small'
        else:
            G.nodes[node]['size'] = None
        G.nodes[node]['visited'] = False
    return G


def size(G, node):
    return G.nodes[node]['size']


def visited(G, node):
    return G.nodes[node]['visited']


def find_paths(G):
    H = G.copy()
    H.clear_edges()
    H = H.to_directed()
    nodes = ['start']
    while nodes:
        neighbors = list()
        for node in nodes:
            if node == 'end':
                pass
            else:
                if size(G, node) != 'big':
                    G.nodes[node]['visited'] = True
                for neighbor in G[node]:
                    if not visited(G, neighbor):
                        # if size(G, neighbor) == 'big':
                        #     nn_len = len(G[neighbor])
                        #     nn_visited = 0
                        #     for nn in G[neighbor]:
                        #         if visited(G, nn):
                        #             nn_visited += 1
                        #         if size(G, nn) == 'big':
                        #             nn_len -= 1
                        #     if nn_visited < nn_len:
                        #         H.add_edge(node, neighbor)
                        #         neighbors.append(neighbor)
                        # else:
                        H.add_edge(node, neighbor)
                        neighbors.append(neighbor)
        nodes = neighbors
    print(H.edges)
    path_count = 0
    for path in nx.all_simple_paths(G, 'start', 'end'):
        print(path)


def main():
    with open("sample.txt") as f:
        data = list(map(str.rstrip, f.readlines()))
        G = generate_graph(data)
    # print(list(nx.all_simple_paths(G, 'start', 'end')))
    print(find_paths(G))


if __name__ == "__main__":
    main()
