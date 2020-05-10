from graphlib import Generator
from graphlib.DirectedGraph import DirectedGraph
from graphlib.Node import Node
from graphlib.algorithms.Algorithms import Algorithms
import os

np_graph = Generator.directed_graph_generator_np(7, 0.7)

np_graph.draw("graph_2.png")


comp = Algorithms().kosaraju(np_graph)
print(comp)


print("------ example ------")
ex_g = DirectedGraph.create_from_file(os.path.dirname(__file__) + "/files/digraph_ex.json", "adjacency_list")
comp2 = Algorithms().kosaraju(ex_g)
print(comp2)

print("------ example ------")
g = DirectedGraph()
g.add_weighted_edge(Node(0), Node(1), weight=-1)
g.add_weighted_edge(Node(1), Node(0), weight=4)
g.add_weighted_edge(Node(0), Node(2), weight=-4)
g.add_weighted_edge(Node(2), Node(1), weight=2)

D = Algorithms().johnson(g)
for i in range(len(D)):
    print(D[i])
