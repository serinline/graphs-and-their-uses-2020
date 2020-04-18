from graphlib import Generator

nl_graph = Generator.graph_generator_nl(10, 7)
print(nl_graph)

np_graph = Generator.graph_generator_np(6, 0.8)
print(np_graph)
