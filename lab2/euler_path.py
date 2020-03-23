from lab1.graph_generator_nl import graph_generator_nl
from lab1.representations import adjacency_matrix


def euler_path(graph):
    path = []
    adj_matrix = adjacency_matrix(graph)

    def dfs_euler(v):
        for u in range(len(graph.edges)):
            if adj_matrix[v][u] > 0:
                adj_matrix[v][u] -= 1
                adj_matrix[u][v] -= 1
                dfs_euler(u)
        path.append(v)

    nodes = list(graph.nodes)
    dfs_euler(nodes[0])
    return path


n = 10
l = 7
G = graph_generator_nl(n, l)
eul = euler_path(G)
print(eul)
