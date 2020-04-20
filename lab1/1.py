import os

from graphlib.Graph import Graph

from graphlib.representations.AdjacencyList import AdjacencyList
from graphlib.representations.AdjacencyMatrix import AdjacencyMatrix

adjency_list_graph = Graph.create_from_file(os.path.dirname(__file__) + "/files/adjacency_list.json", "adjacency_list")
print(adjency_list_graph)

adjency_matrix_graph = Graph.create_from_file(os.path.dirname(__file__) + "/files/adjacency_matrix.json", "adjacency_matrix")
print(adjency_matrix_graph)

indience_matrix_graph = Graph.create_from_file(os.path.dirname(__file__) + "/files/incidence_matrix.json", "incidence_matrix")
print(indience_matrix_graph)
AdjacencyMatrix(indience_matrix_graph).print()
AdjacencyList(indience_matrix_graph).print()
