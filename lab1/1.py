import os

from graphlib.Graph import Graph

adjacency_list_graph = Graph.create_from_file(os.path.dirname(__file__) + "/files/adjacency_list.json", "adjacency_list")
print(adjacency_list_graph)

adjacency_matrix_graph = Graph.create_from_file(os.path.dirname(__file__) + "/files/adjacency_matrix.json", "adjacency_matrix")
print(adjacency_matrix_graph)
incidence_matrix_graph = Graph.create_from_file(os.path.dirname(__file__) + "/files/incidence_matrix.json", "incidence_matrix")
print(incidence_matrix_graph)
