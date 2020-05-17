import os
from graphlib.DirectedGraph import DirectedGraph
from graphlib.algorithms.Algorithms import Algorithms

graph = DirectedGraph.create_from_file(os.path.dirname(__file__) + "/files/pagerank_list.json", "adjacency_list")

dict = Algorithms().pagerank_randomwalk(graph)

print(dict)