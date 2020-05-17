from operator import attrgetter

import networkx as nx
import matplotlib.pyplot as plt


class Drawer:

    @classmethod
    def draw(cls, our_graph, file_name: str, special_edges = None) -> None:
        graph = nx.Graph()

        for node in our_graph.get_nodes():
            graph.add_node(node.get_id())

        edges = our_graph.get_edges()
        edges.sort(key=attrgetter("nodes"))

        for edge in edges:
            nodes_ids = edge.get_nodes_ids()
            if our_graph.get_is_weighted():
                graph.add_edge(nodes_ids[0].get_id(), nodes_ids[1].get_id(), weight=edge.get_weight())
            else:
                graph.add_edge(nodes_ids[0].get_id(), nodes_ids[1].get_id())

        labels = {}
        for i in range(len(our_graph.get_nodes())):
            labels[i] = i + 1

        pos = nx.circular_layout(graph)

        nx.draw(graph, pos, labels=labels)

        if our_graph.get_is_weighted():
            nx.draw_networkx_edge_labels(graph, pos, edge_labels=nx.get_edge_attributes(graph, "weight"))

        edges_list_special = []

        if special_edges is not None:
            for e in special_edges:
                nodes = e.get_nodes_ids()
                node_1_id = nodes[0].get_id()
                node_2_id = nodes[1].get_id()
                edges_list_special.append((node_1_id, node_2_id))

        if len(edges_list_special) != 0:
            nx.draw_networkx_edges(graph, pos,
                                   edgelist=edges_list_special,
                                   width=8, alpha=0.5, edge_color='b')

        plt.axis("equal")

        plt.savefig(file_name, format="png")
        plt.clf()

    @classmethod
    def draw_directed(cls, di_graph, file_name: str = None) -> None:
        graph = nx.DiGraph()

        for node in di_graph.get_nodes():
            graph.add_node(node.get_id())

        edges = di_graph.get_edges()
        edges.sort(key=attrgetter("nodes"))

        for edge in edges:
            nodes_ids = edge.get_nodes_ids()
            graph.add_edge(nodes_ids[0].get_id(), nodes_ids[1].get_id(), weight=edge.get_weight())

        labels = {}
        for i in range(len(di_graph.get_nodes())):
            labels[i] = i + 1

        edge_labels = dict([((u, v,), d['weight'])
                            for u, v, d in graph.edges(data=True)])

        pos = nx.circular_layout(graph)
        nx.draw(graph, pos, labels=labels, connectionstyle='arc3, rad = 0.1')
        nx.draw_networkx_edge_labels(graph, pos, labels=labels, edge_labels=edge_labels, label_pos=0.3)
        plt.axis("equal")

        plt.savefig(file_name, format="png")
        plt.clf()


    @classmethod
    def draw_flow_network(cls, fn, file_name: str = None, special_edges = None) -> None:
        graph = nx.DiGraph()

        for node in fn.get_nodes():
            graph.add_node(node.get_id())
        

        edges = fn.get_edges()
        edges.sort(key=attrgetter("nodes"))

        for edge in edges:
            nodes_ids = edge.get_nodes_ids()
            graph.add_edge(nodes_ids[0].get_id(), nodes_ids[1].get_id(), capacity=edge.get_capacity(), flow=edge.get_flow())

        labels = {}
        for i in range(len(fn.get_nodes())):
            labels[i] = i + 1

        edge_labels = dict([((u, v,), str(d['flow']) + '/' + str(d['capacity']))
                            for u, v, d in graph.edges(data=True)])


        pos = nx.circular_layout(graph)
        nx.draw(graph, pos, labels=labels, connectionstyle='arc3, rad = 0.1')
        nx.draw_networkx_edge_labels(graph, pos, labels=labels, edge_labels=edge_labels, label_pos=0.3)
        
        edges_list_special = []

        if special_edges is not None:
            for e in special_edges:
                nodes = e.get_nodes_ids()
                node_1_id = nodes[0].get_id()
                node_2_id = nodes[1].get_id()
                edges_list_special.append((node_1_id, node_2_id))

        if len(edges_list_special) != 0:
            nx.draw_networkx_edges(graph, pos,
                                   edgelist=edges_list_special,
                                   width=8, alpha=0.5, edge_color='b')

        
        plt.axis("equal")

        plt.savefig(file_name, format="png")
        plt.clf()
