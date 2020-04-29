import os
import numpy as np

from graphlib import Generator
from graphlib.DirectedGraph import DirectedGraph
from graphlib.algorithms.Algorithms import Algorithms
from graphlib.drawer.drawer import DirectedDrawer
from graphlib.representations.AdjacencyList import DirectedAdjacencyList
from graphlib.representations.AdjacencyMatrix import DirectedAdjacencyMatrix
from graphlib.representations.IncidenceMatrix import DirectedIncidenceMatrix

directed_adjacency_list_graph = DirectedGraph.create_from_file(os.path.dirname(__file__) + "/files/directed_adjacency_list.json", "adjacency_list")
# print(directed_adjacency_list_graph)
#
directed_adjacency_matrix_graph = DirectedGraph.create_from_file(os.path.dirname(__file__) + "/files/directed_adjacency_matrix.json", "adjacency_matrix")
# print(directed_adjacency_matrix_graph)
#
# directed_incidence_matrix_graph = DirectedGraph.create_from_file(os.path.dirname(__file__) + "/files/directed_incidence_matrix.json", "incidence_matrix")
# print(directed_incidence_matrix_graph)
#
# np_graph = Generator.directed_graph_generator_np(6, 0.8)
# print(np_graph)

# DirectedAdjacencyMatrix(directed_adjacency_list_graph).print()

# alg = Algorithms()
# conf = alg.kosaraju(directed_adjacency_list_graph)
# print(conf)

drawer = DirectedDrawer()
drawer.draw(directed_adjacency_list_graph, "graph.png")

# g = DirectedAdjacencyMatrix(directed_adjacency_list_graph)
# g.print()
# g1 = np.array(g.matrix).T
# print(g1)
# # for i in graph_T:
# #     print(i)