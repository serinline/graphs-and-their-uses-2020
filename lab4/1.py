import os

from graphlib.DirectedGraph import DirectedGraph
from graphlib.representations.AdjacencyList import DirectedAdjacencyList
from graphlib.representations.AdjacencyMatrix import DirectedAdjacencyMatrix

directed_adjacency_list_graph = DirectedGraph.create_from_file(os.path.dirname(__file__) + "/files/directed_adjacency_list.json", "adjacency_list")
print(directed_adjacency_list_graph)

directed_adjacency_matrix_graph = DirectedGraph.create_from_file(os.path.dirname(__file__) + "/files/directed_adjacency_matrix.json", "adjacency_matrix")
print(directed_adjacency_matrix_graph)

directed_incidence_matrix_graph = DirectedGraph.create_from_file(os.path.dirname(__file__) + "/files/directed_incidence_matrix.json", "incidence_matrix")
print(directed_incidence_matrix_graph)

DirectedAdjacencyList(directed_incidence_matrix_graph).print()
