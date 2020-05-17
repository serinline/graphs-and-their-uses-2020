from graphlib import Generator
from graphlib.DirectedGraph import DirectedGraph
from graphlib.Node import Node
from graphlib.algorithms.Algorithms import Algorithms
import os

from graphlib.representations.AdjacencyList import DirectedAdjacencyList

np_graph = Generator.directed_graph_generator_np(5, 0.7)

np_graph.draw("graph_2.png")


print("ilość spójnych składowych:", np_graph.SCCs(np_graph))

DirectedAdjacencyList(np_graph).print()


print("------ example ------")
# ex_g = DirectedGraph.create_from_file(os.path.dirname(__file__) + "/files/digraph_ex.json", "adjacency_list")
ex_g = DirectedGraph.create_from_file(os.path.dirname(__file__) + "/files/example.json", "adjacency_list")
DirectedAdjacencyList(ex_g).print()

comp3 = ex_g.SCCs(ex_g)
print("ilość spójnych składowych:", comp3)

print("------ example ------")
g = DirectedGraph()
g.add_weighted_edge(Node(0), Node(1), weight=-1)
g.add_weighted_edge(Node(1), Node(0), weight=4)
g.add_weighted_edge(Node(0), Node(2), weight=-4)
g.add_weighted_edge(Node(2), Node(1), weight=2)

D = Algorithms().johnson(g)
for i in range(len(D)):
    print(D[i])
