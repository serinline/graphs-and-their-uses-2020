import networkx
import matplotlib.pyplot as plot

from lab1.graph_generator_nl import graph_generator_nl
from lab1.representations import adjacency_matrix


def euler_cycle(graph):
    cycle = []
    adj_matrix = adjacency_matrix(graph)
    plot

    def dfs_euler(v):
        for u in range(len(graph.edges)):
            if adj_matrix[v][u] > 0:
                adj_matrix[v][u] -= 1
                adj_matrix[u][v] -= 1
                dfs_euler(u)
        cycle.append(v)

    nodes = list(graph.nodes)
    dfs_euler(nodes[0])
    return cycle


n = 10
l = 7
G = graph_generator_nl(n, l)
eul = euler_cycle(G)
pos = networkx.circular_layout(G)
networkx.draw_networkx(G, pos)
plot.show()
print(eul)
