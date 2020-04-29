from operator import attrgetter

import networkx as nx
import matplotlib.pyplot as plt


class Drawer:

    @classmethod
    def draw(cls, our_graph, file_name: str) -> None:
        graph = nx.Graph()

        for node in our_graph.get_nodes():
            graph.add_node(node.get_id())

        edges = our_graph.get_edges()
        edges.sort(key=attrgetter("nodes"))

        for edge in edges:
            nodes_ids = edge.get_nodes_ids()
            graph.add_edge(nodes_ids[0].get_id(), nodes_ids[1].get_id())

        labels = {}
        for i in range(len(our_graph.get_nodes())):
            labels[i] = i + 1

        nx.draw_circular(graph, labels=labels)
        plt.axis("equal")

        plt.savefig(file_name, format="png")
        plt.clf()


class DirectedDrawer:

    @classmethod
    def draw(cls, our_graph, file_name: str = None) -> None:
        graph = nx.DiGraph()

        edges = our_graph.get_edges()
        edges.sort(key=attrgetter("nodes"))
        print(edges[0])

        for edge in edges:
            nodes_ids = edge.get_nodes_ids()
            graph.add_edge(nodes_ids[0].get_id(), nodes_ids[1].get_id())

        labels = {}
        for i in range(len(our_graph.get_nodes())):
            labels[i] = i + 1

        nx.draw_circular(graph, labels=labels)
        plt.axis("equal")

        plt.savefig(file_name, format="png")
        plt.clf()
