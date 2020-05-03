from graphlib.algorithms.Algorithms import Algorithms
from graphlib.Generator import graph_generator_consistent_weighted

g = graph_generator_consistent_weighted(7, 1, 10)
g.draw("graph_weighted.png")

center = Algorithms.get_graph_center(g)
print(center)

center_minimax = Algorithms.get_graph_center_minimax(g)
print(center_minimax)
