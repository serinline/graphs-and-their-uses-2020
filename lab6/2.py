import os
from graphlib.Graph import Graph
from graphlib.algorithms.Algorithms import Algorithms

graph = Graph.create_from_file(os.path.dirname(__file__) + "/files/travelling_salesman.json", "coordinates")

p = Algorithms.simulated_annealing(graph)
print(p)

