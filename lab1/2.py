from graphlib import Generator

nl_graph = Generator.graph_generator_nl(10, 7)
print(nl_graph)
nl_graph.draw("nl_graph.png")
