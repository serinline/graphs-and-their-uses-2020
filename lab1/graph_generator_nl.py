import matplotlib.pyplot as plot
import networkx
from itertools import combinations
from random import sample


def graph_generator_nl(n, l):
    V = set([v for v in range(n)])
    E = set()

    comb = combinations(V, 2)
    random_comb = sample(list(comb), l)
    for c in random_comb:
        E.add(c)

    graph = networkx.Graph()
    graph.add_nodes_from(V)
    graph.add_edges_from(E)

    return graph

# test
# n = 10
# l = 7
# G = GraphGeneratorNL(n, l)

# pos = networkx.circular_layout(G)
# networkx.draw_networkx(G, pos)
# plot.show()
