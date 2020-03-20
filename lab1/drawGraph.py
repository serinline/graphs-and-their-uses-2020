import random
import math
import matplotlib.pyplot as plt
from GraphGeneratorNL import GraphGeneratorNL as gr
import networkx 


def draw(graph):
    x = []
    y = []
    nodes = list(graph.nodes)
    for n in range(len(nodes)):
        angle = random.uniform(0,6)*(math.pi*2)
        x.append(math.cos(angle))
        y.append(math.sin(angle))
    plt.scatter(x,y)
    plt.axes().set_aspect('equal', 'datalim')
    plt.show()


n = 10
l = 7
G = gr(n, l)
draw(G)