from graphlib.Graph import Graph

import numpy as np

from typing import List

from graphlib.Edge import Edge
from graphlib.Node import Node
from graphlib.drawer.drawer import Drawer


class DirectedGraph(Graph):

    @classmethod
    def create_graph_from_adjacency_list(cls, input_data: List[List[int]]):
        edges = list()
        for index, i in enumerate(input_data):
            for j in i:
                edges.append((Node(index), Node(j)))

        graph = DirectedGraph()
        graph.add_edges_from(edges)
        return graph

    @classmethod
    def create_graph_from_adjacency_matrix(cls, input_data: List[List[int]]):
        edges = list()
        for index_i, i in enumerate(input_data):
            for index_j, j in enumerate(i):
                if j == 1:
                    edges.append((Node(index_i), Node(index_j)))

        graph = DirectedGraph()
        graph.add_edges_from(edges)
        return graph

    @classmethod
    def create_graph_from_incidence_matrix(cls, input_data: List[List[int]]):
        edges = list()

        transposed = np.array(input_data).T

        for i in transposed:
            first_node = None
            second_node = None
            for index_j, j in enumerate(i):
                if j == -1:
                    first_node = index_j
                if j == 1:
                    second_node = index_j
            edges.append((Node(first_node), Node(second_node)))

        graph = DirectedGraph()
        graph.add_edges_from(edges)
        return graph

    def add_edge(self, first_node: Node, second_node: Node) -> None:
        self.nodes.add(first_node)
        self.nodes.add(second_node)
        self.edges.append(Edge(first_node, second_node))

    def add_edges(self, edges: List[Edge]):
        self.edges = edges

    def add_edges_from(self, edges: List[tuple]) -> None:
        for edge in edges:
            if self.is_weighted:
                self.add_weighted_edge(edge[0], edge[1], edge[2])
            else:
                self.add_edge(edge[0], edge[1])

    def draw(self, file_name: str = "graph.png") -> None:
        Drawer.draw_directed(self, file_name)

    def transponse(self, g):
        edges = g.get_edges()
        for edge in edges:
            tmp = edge.get_nodes_ids()
            new_edge = (tmp[1], tmp[0])
            edge.set_nodes_ids(new_edge)
        return g

    def copy(self):
        copied = DirectedGraph()
        for n in self.get_nodes():
            copied.nodes.add(n)
        e = list()
        for edge in self.get_edges():
            nds = edge.get_nodes_ids()
            w = edge.get_weight()
            e.append((nds[0], nds[1], w))
        copied.is_weighted = True
        copied.add_edges_from(e)
        return copied

    def add_weighted_edge(self, first_node: Node, second_node: Node, weight: int) -> None:
        self.nodes.add(first_node)
        self.nodes.add(second_node)
        self.edges.append(Edge(first_node, second_node, weight=weight))

    def find_directed_edge(self, node_1: int, node_2: int) -> Edge:
        for e in self.get_edges():
            nodes = e.get_nodes_ids()
            nodes_1 = nodes[0].get_id()
            nodes_2 = nodes[1].get_id()
            if (nodes_1 == node_1 and nodes_2 == node_2):
                return e
    
    def is_edge_in_graph(self, node_1: int, node_2: int) -> bool:
        for e in self.get_edges():
            nodes = e.get_nodes_ids()
            nodes_1 = nodes[0].get_id()
            nodes_2 = nodes[1].get_id()
            if (nodes_1 == node_1 and nodes_2 == node_2):
                return True
        
        return False
