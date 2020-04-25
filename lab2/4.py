from graphlib import Generator
from graphlib.algorithms.Algorithms import Algorithms

while True:
    nl_graph = Generator.graph_generator_np(8, 0.5)
    if nl_graph.is_euler():
        break

nl_graph.draw()
print(Algorithms.euler_cycle(nl_graph))
