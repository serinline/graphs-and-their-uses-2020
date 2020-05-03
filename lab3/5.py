from graphlib.algorithms.Algorithms import Algorithms
from graphlib.Generator import graph_generator_consistent_weighted

g = graph_generator_consistent_weighted(7, 1, 10)
g.draw("graph_weighted.png")

minimal_tree = Algorithms.prim(g)
print(minimal_tree)
g.draw("graph_weighted_with_tree.png", minimal_tree)
