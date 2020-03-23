import random
import math
import matplotlib.pyplot as plt
from lab1.graph_generator_nl import graph_generator_nl as gr
import networkx 


def draw(graph):
    x = []
    y = []
    nodes_from = list()
    nodes_to = list()
    nodes = list(graph.nodes)
    print(nodes)
    for n in range(len(nodes)):
        angle = random.uniform(0,1)*(math.pi*2)
        x.append(math.cos(angle))
        y.append(math.sin(angle))
    plt.scatter(x,y)
    plt.axes().set_aspect('equal', 'datalim')
    # for node in graph.nodes():
    #     plt.plot(node)

    for edge in graph.edges():
        nodes_from.append(edge[0])
        nodes_to.append(edge[1])
        plt.plot(edge)

    #plt.plot(nodes_from, nodes_to)
    plt.show()



n = 10
l = 7
G = gr(n, l)
draw(G)