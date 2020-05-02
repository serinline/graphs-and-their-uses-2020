import random

from graphlib import Generator
from graphlib.DirectedGraph import DirectedGraph
from graphlib.algorithms.Algorithms import Algorithms

np_graph = Generator.directed_graph_generator_np(6, 0.8)

np_graph.draw("graph.png")

comp = Algorithms().kosaraju(np_graph)
result = all(elem == comp[0] for elem in comp)

if result:
    for edge in np_graph.get_edges():
        weight = random.randint(-5, 10)
        edge.set_weight(weight)
