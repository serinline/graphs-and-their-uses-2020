from graphlib import Generator
from graphlib.DirectedGraph import DirectedGraph
from graphlib.algorithms.Algorithms import Algorithms
import os

np_graph = Generator.directed_graph_generator_np(5, 0.7)

np_graph.draw("graph_2.png")


alg = Algorithms()
comp = alg.kosaraju(np_graph)
print(comp)


print("------ example ------")
ex_g = DirectedGraph.create_from_file(os.path.dirname(__file__) + "/files/digraph_ex.json", "adjacency_list")
comp2 = alg.kosaraju(ex_g)
print(comp2)
