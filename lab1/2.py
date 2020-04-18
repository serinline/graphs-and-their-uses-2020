import os

from graphlib.Graph import Graph
from graphlib.representations.AdjencyList import AdjencyList
from graphlib.representations.IncidenceMatrix import IncidenceMatrix

adjency_matrix_graph_1 = Graph.create_from_file(os.path.dirname(__file__) + "/files/adjency_matrix_1.json", "adjency_matrix")
# Tutaj numerowanie jest od zera, dlatego wynik jest inny niż na przykładzie od dr. Strzałki
AdjencyList(adjency_matrix_graph_1).print()
IncidenceMatrix(adjency_matrix_graph_1).print()
adjency_matrix_graph_1.draw("nl_graph.png")
