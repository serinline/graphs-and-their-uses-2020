import networkx
import matplotlib.pyplot as plot

from graphlib.Generator import graph_generator_nl
from graphlib.representations.AdjacencyMatrix import AdjacencyMatrix


def euler_cycle(graph):
    cycle = []
    adj_matrix = AdjacencyMatrix(graph)
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
