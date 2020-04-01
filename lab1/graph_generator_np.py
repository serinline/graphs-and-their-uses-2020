import matplotlib.pyplot as plot
import networkx
from itertools import combinations
from random import random


def graph_generator_np(n, p):
    v = set([v for v in range(n)])
    e = set()

    for c in combinations(v, 2):
        tmp = random()
        if tmp < p:
            e.add(c)

    graph = networkx.Graph()
    graph.add_nodes_from(v)
    graph.add_edges_from(e)

    return graph


# test
n = 6
p = 0.8
G = graph_generator_np(n, p)
pos = networkx.circular_layout(G)
networkx.draw_networkx(G, pos)
plot.show()