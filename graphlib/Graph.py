import json

import numpy as np

from typing import List, Set

from graphlib.Edge import Edge
from graphlib.Node import Node

from graphlib.drawer.drawer import Drawer


class Graph:
    """
    Class representing single Graph
    """
    edges: List[Edge]
    nodes: Set[Node]

    # TODO: Probably we want to add here type of graph (weighted etc.)

    def __init__(self, edges: List[Edge] = None, nodes: Set[Node] = None):
        if edges is None:
            edges = []
        if nodes is None:
            nodes = set()
        self.edges = edges
        self.nodes = nodes

    @classmethod
    def create_from_file(cls, file_name: str, representation_type: str):
        with open(file_name) as file:
            json_content = json.load(file)
            input_data = json_content["input"]

            if representation_type == "adjacency_list":
                return cls.create_graph_from_adjacency_list(input_data)
            if representation_type == "adjacency_matrix":
                return cls.create_graph_from_adjacency_matrix(input_data)
            if representation_type == "incidence_matrix":
                return cls.create_graph_from_incidence_matrix(input_data)

            raise Exception("Incorrect representation type!")

    @classmethod
    def create_graph_from_adjacency_list(cls, input_data: List[List[int]]):
        edges = set()
        for index, i in enumerate(input_data):
            for j in i:
                edges.add((index, j))

        graph = Graph()
        graph.add_edges_from(edges)
        return graph

    @classmethod
    def create_graph_from_adjacency_matrix(cls, input_data: List[List[int]]):
        edges = set()
        for index_i, i in enumerate(input_data):
            for index_j, j in enumerate(i):
                if j == 1:
                    edges.add((index_i, index_j))

        graph = Graph()
        graph.add_edges_from(edges)
        return graph

    @classmethod
    def create_graph_from_incidence_matrix(cls, input_data: List[List[int]]):
        edges = set()

        transposed = np.array(input_data).T

        for i in transposed:
            first_node = None
            second_node = None
            for index_j, j in enumerate(i):
                if j == 1:
                    if first_node is None:
                        first_node = index_j
                    else:
                        second_node = index_j
                        break
            edges.add((first_node, second_node))

        graph = Graph()
        graph.add_edges_from(edges)
        return graph

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"Graph(\n\tNodes=[${self.nodes}]\n\tEdges=[${self.edges}]\n)"

    def __eq__(self, other) -> bool:
        return self.edges == other.edges and self.nodes == other.nodes

    def add_edge(self, first_node: Node, second_node: Node) -> None:
        self.nodes.add(first_node)
        self.nodes.add(second_node)

        has_edge = next((x for x in self.edges if x.get_nodes_ids()[0] == second_node and x.get_nodes_ids()[1] == first_node), None)
        if has_edge is None:
            self.edges.append(Edge(first_node, second_node))

    def add_edges_from(self, edges: Set[tuple]) -> None:
        for edge in edges:
            self.add_edge(edge[0], edge[1])

    def get_edges(self) -> List[Edge]:
        return self.edges

    def get_nodes(self) -> Set[Node]:
        return self.nodes

    def draw(self, file_name: str = "graph.png") -> None:
        Drawer.draw(self, file_name)
