import random

from graphlib import Generator
from graphlib.algorithms.Algorithms import Algorithms

# zadanie 1 + 2
result = False
while not result:
    np_graph = Generator.directed_graph_generator_np(6, 0.4)
    comp = Algorithms().kosaraju(np_graph)
    result = all(elem == comp[0] for elem in comp)

# zadania 3 + 4
for edge in np_graph.get_edges():
    weight = random.randint(-1, 10)
    edge.set_weight(weight)

np_graph.draw("digraph.png")
D = Algorithms().johnson(np_graph)
for i in range(len(D)):
    print(D[i])
