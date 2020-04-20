import os

from graphlib.Graph import Graph

from graphlib.representations.AdjencyList import AdjencyList
from graphlib.representations.AdjencyMatrix import AdjencyMatrix

adjency_list_graph = Graph.create_from_file(os.path.dirname(__file__) + "/files/adjency_list.json", "adjency_list")
print(adjency_list_graph)

adjency_matrix_graph = Graph.create_from_file(os.path.dirname(__file__) + "/files/adjency_matrix.json", "adjency_matrix")
print(adjency_matrix_graph)

indience_matrix_graph = Graph.create_from_file(os.path.dirname(__file__) + "/files/indience_matrix.json", "indience_matrix")
print(indience_matrix_graph)
AdjencyMatrix(indience_matrix_graph).print()
AdjencyList(indience_matrix_graph).print()
