import matplotlib.pyplot as plot
import networkx
from itertools import combinations
from random import sample

from lab1.Graph import Graph


def graph_generator_nl(n, l):
    v = set([v for v in range(n)])
    e = set()

    comb = combinations(v, 2)
    random_comb = sample(list(comb), l)
    for c in random_comb:
        e.add(c)

    graph = Graph()
    #graph.add_nodes_from(v)
    graph.add_edges_from(e)

    return graph

# test
n = 10
l = 7
G = graph_generator_nl(n, l)

#G.print_edges()
# pos = networkx.circular_layout(G)
# networkx.draw_networkx(G, pos)
# plot.show()
