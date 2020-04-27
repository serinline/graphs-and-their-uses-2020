import os

from graphlib import Generator
from graphlib.Graph import Graph
from graphlib.algorithms.Algorithms import Algorithms

hamilton = Graph.create_from_file(os.path.dirname(__file__) + "/files/hamilton.json", "adjacency_list")
hamilton.draw()
print(Algorithms.hamilton_cycle(hamilton))

np_graph = Generator.graph_generator_np(6, 0.1)
print(Algorithms.hamilton_cycle(np_graph))
