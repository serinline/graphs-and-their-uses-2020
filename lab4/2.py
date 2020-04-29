from graphlib import Generator
from graphlib.algorithms.Algorithms import Algorithms
from graphlib.drawer.drawer import DirectedDrawer

np_graph = Generator.directed_graph_generator_np(6, 0.8)

drawer = DirectedDrawer()
drawer.draw(np_graph, "graph_2.png")

alg = Algorithms()
comp = alg.kosaraju(np_graph)
print(comp)
