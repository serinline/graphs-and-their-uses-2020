from graphlib import Generator
from graphlib.algorithms.Algorithms import Algorithms
import random

alg = Algorithms()

result = False
while not result:
    np_graph = Generator.directed_graph_generator_np(5, 0.8)
    comp = alg.kosaraju(np_graph)
    result = all(elem == comp[0] for elem in comp)


np_graph.is_weighted = True
for edge in np_graph.get_edges():
    weight = random.randint(-5, 10)
    edge.set_weight(weight)

np_graph.draw("graph_3.png")

val, d_s = alg.bellman_ford(np_graph, 4)
print(val, d_s)
