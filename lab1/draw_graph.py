import matplotlib.pyplot as plt
import numpy as np
from lab1.graph_generator_nl import graph_generator_nl as gr
from lab1.representations import adjacency_list


# to fix  - too many edges
def draw(graph):
    nodes = list(graph.nodes)
    plt.figure(figsize=(5, 5))
    num_nodes = len(nodes)
    angle = np.linspace(0, 2*np.pi, num_nodes)
    cx, cy = (10, 10)
    radius = 5.0
    graph_list = adjacency_list(graph)

    for i in range(num_nodes):
        x_node = cx + radius*np.cos(angle)
        y_node = cy - radius*np.sin(angle)
        plt.scatter(x_node, y_node, c='blue', s=50)
        for node in graph_list[i]:
            next_angle = angle*node
            x_next_node = cx + radius*np.cos(next_angle)
            y_next_node = cy - radius*np.sin(next_angle)
            x_values = [x_node, x_next_node]
            y_values = [y_node, y_next_node]
            plt.plot(x_values, y_values)
    plt.show()


n = 8
l = 6
G = gr(n, l)
draw(G)