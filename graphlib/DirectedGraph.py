from graphlib.Graph import Graph

import numpy as np

from typing import List

from graphlib.Edge import Edge
from graphlib.Node import Node
from graphlib.drawer.drawer import Drawer


class DirectedGraph(Graph):

    def __init__(self):
        super().__init__()

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

    def add_edges_from(self, edges: List[tuple]) -> None:
        for edge in edges:
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
