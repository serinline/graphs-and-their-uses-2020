from graphlib import Generator
from graphlib.algorithms.Algorithms import Algorithms


alg = Algorithms()

result = False;
while not result:
    np_graph = Generator.directed_graph_generator_np(5, 1)
    comp = alg.kosaraju(np_graph)
    result = all(elem == comp[0] for elem in comp)

np_graph.draw("graph_3.png")