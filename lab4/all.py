import random

from graphlib import Generator
from graphlib.algorithms.Algorithms import Algorithms

# zadanie 1 + 2
result = 0
while result != 1:
    np_graph = Generator.directed_graph_generator_np(6, 1)
    result = np_graph.SCCs(np_graph)

# zadania 3 + 4
for edge in np_graph.get_edges():
    weight = random.randint(-1, 10)
    edge.set_weight(weight)

np_graph.draw("digraph.png")
D = Algorithms().johnson(np_graph)
for i in range(len(D)):
    print(D[i])
