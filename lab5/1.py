import os
from graphlib.DirectedGraph import DirectedGraph
from graphlib import Generator
from graphlib.algorithms.Algorithms import Algorithms


flow_network = Generator.flow_network_generator(3)

print(Algorithms.ford_fulkerson(flow_network, 0, len(flow_network.get_nodes())-1))

flow_network.draw("graph.png")
