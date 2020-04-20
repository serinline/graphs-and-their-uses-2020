import os

from graphlib.Graph import Graph
from graphlib.representations.AdjacencyList import AdjacencyList
from graphlib.representations.IncidenceMatrix import IncidenceMatrix

adjacency_matrix_graph_1 = Graph.create_from_file(os.path.dirname(__file__) + "/files/adjacency_matrix_1.json", "adjacency_matrix")
# Tutaj numerowanie jest od zera, dlatego wynik jest inny niż na przykładzie od dr. Strzałki
AdjacencyList(adjacency_matrix_graph_1).print()
IncidenceMatrix(adjacency_matrix_graph_1).print()
adjacency_matrix_graph_1.draw("nl_graph.png")
