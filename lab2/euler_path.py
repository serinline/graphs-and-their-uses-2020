from lab1.graph_generator_nl import graph_generator_nl
from lab1.representations import adjacency_list


def euler_path(graph):
    path = set()
    adj_list = adjacency_list(graph)
    edges = list(graph.edges)
    print(edges)
    dfs_euler(adj_list, edges, path)
    return path


def dfs_euler(adj_list, edges, path):
    for v in adj_list:
        for u in adj_list[v]:
            to_del = (v, u)
            edges.remove(to_del)
            dfs_euler(adj_list, edges, path)
        path.add(v)


n = 10
l = 7
G = graph_generator_nl(n, l)
eul = euler_path(G)
print(eul)
