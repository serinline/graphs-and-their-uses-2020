from graphlib import Generator

while True:
    nl_graph = Generator.graph_generator_np(8, 0.5)
    if nl_graph.is_k_regular(2):
        break

nl_graph.draw()
