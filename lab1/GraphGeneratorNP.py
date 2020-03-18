import matplotlib.pyplot as plot
import networkx
from itertools import combinations
from random import random


def GraphGeneratorNP(n, p):
    V = set([v for v in range(n)])
    E = set()

    for c in combinations(V, 2):
        tmp = random()
        if tmp < p:
            E.add(c)

    graph = networkx.Graph()
    graph.add_nodes_from(V)
    graph.add_edges_from(E)

    return graph



#test
n = 6
p = 0.8
G = GraphGeneratorNP(n, p)
pos = networkx.circular_layout(G)
networkx.draw_networkx(G, pos)
plot.show()