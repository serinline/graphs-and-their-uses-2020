from graphlib.algorithms.Algorithms import Algorithms
from graphlib.Generator import graph_generator_consistent_weighted

g = graph_generator_consistent_weighted(7, 1, 10)
g.draw("graph_weighted.png")

from_node = 0
nodes = g.get_nodes()
for i in range(len(nodes)):
    distance, path = Algorithms.dijkstra(g, from_node, i)
    print(f"d({i}) = {distance} ==> {path}")
