import matplotlib.pyplot as plt
import numpy as np
from lab1.graph_generator_nl import graph_generator_nl as gr


def draw(graph):
    nodes = list(graph.nodes)
    fig = plt.figure(figsize=(5, 5))
    num_nodes = len(nodes)
    angle = np.linspace(0, 2*np.pi, num_nodes)
    cx, cy = (10, 10)
    radius = 5.0
    x_node = cx + radius*np.cos(angle)
    y_node = cy + radius*np.sin(angle)

    plt.scatter(x_node, y_node, c = 'blue', s=30)
    plt.show()




n = 10
l = 7
G = gr(n, l)
draw(G)