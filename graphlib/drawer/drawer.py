from operator import attrgetter

import networkx as nx
import matplotlib.pyplot as plt


class Drawer:
    @classmethod
    def draw(cls, our_graph, file_name: str) -> None:
        graph = nx.Graph()

        for node in our_graph.get_nodes():
            graph.add_node(node)

        edges = our_graph.get_edges()
        edges.sort(key=attrgetter("nodes"))

        for edge in edges:
            nodes_ids = edge.get_nodes_ids()
            graph.add_edge(nodes_ids[0], nodes_ids[1])

        labels = {}
        for i in range(len(our_graph.get_nodes())):
            labels[i] = i + 1

        nx.draw_circular(graph, labels=labels)
        plt.axis("equal")

        plt.savefig(file_name, format="png")
        plt.clf()

