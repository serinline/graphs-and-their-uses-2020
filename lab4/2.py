from graphlib import Generator
from graphlib.algorithms.Algorithms import Algorithms

np_graph = Generator.directed_graph_generator_np(5, 0.7)

np_graph.draw("graph_2.png")

alg = Algorithms()
comp = alg.kosaraju(np_graph)
print(comp)
