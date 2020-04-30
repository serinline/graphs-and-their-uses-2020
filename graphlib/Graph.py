import json
import random
from operator import itemgetter

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
                edges.add((Node(index), Node(j)))

        graph = Graph()
        graph.add_edges_from(edges)
        return graph

    @classmethod
    def create_graph_from_adjacency_matrix(cls, input_data: List[List[int]]):
        edges = set()
        for index_i, i in enumerate(input_data):
            for index_j, j in enumerate(i):
                if j == 1:
                    edges.add((Node(index_i), Node(index_j)))

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
            edges.add((Node(first_node), Node(second_node)))

        graph = Graph()
        graph.add_edges_from(edges)
        return graph

    @classmethod
    def create_graph_from_graphic_sequence(cls, input_data: List[int]):
        indexed_data = [[index, idx] for index, idx in enumerate(input_data)]

        adjacency_list = [[] for _ in range(len(indexed_data))]

        for _ in range(len(indexed_data)):
            indexed_data.sort(reverse=True, key=itemgetter(1))
            i = 0
            j = i + 1
            while indexed_data[i][1] > 0 and j < len(indexed_data):
                adjacency_list[indexed_data[i][0]].append(indexed_data[j][0])
                adjacency_list[indexed_data[j][0]].append(indexed_data[i][0])
                indexed_data[i][1] -= 1
                indexed_data[j][1] -= 1
                j += 1

        return cls.create_graph_from_adjacency_list(adjacency_list)

    @classmethod
    def components_recursive_helper(cls, nr: int, v, g, comp: List[int]):
        edges = g.get_edges()
        neighbours = []

        for edge in edges:
            nodes = edge.get_nodes_ids()
            if nodes[0].get_id() == v:
                neighbours.append(nodes[1].get_id())
                continue
            if nodes[1].get_id() == v:
                neighbours.append(nodes[0].get_id())
                continue

        for u in neighbours:
            if comp[u] == -1:
                comp[u] = nr
                Graph.components_recursive_helper(nr, u, g, comp)

    @classmethod
    def find_neighbours(cls, v, g) -> List[int]:
        neighbours = list()
        edges = cls.get_edges(g)
        for edge in edges:
            nodes = edge.get_nodes_ids()
            if nodes[0].get_id() == v:
                neighbours.append(nodes[1].get_id())
                continue
            if nodes[1].get_id() == v:
                neighbours.append(nodes[0].get_id())
                continue
        return neighbours

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"Graph(\n\tNodes=[${self.nodes}]\n\tEdges=[${self.edges}]\n)"

    def __eq__(self, other) -> bool:
        return self.edges == other.edges and self.nodes == other.nodes

    def add_edge(self, first_node: Node, second_node: Node) -> None:
        self.nodes.add(first_node)
        self.nodes.add(second_node)

        has_edge = next(
            (x for x in self.edges if x.get_nodes_ids()[0] == second_node and x.get_nodes_ids()[1] == first_node), None)
        if has_edge is None:
            self.edges.append(Edge(first_node, second_node))

    def remove_edge(self, e: Edge):
        self.edges.remove(e)

    def add_edges_from(self, edges: Set[tuple]) -> None:
        for edge in edges:
            self.add_edge(edge[0], edge[1])

    def add_node(self, node: Node):
        self.nodes.add(node)

    def get_edges(self) -> List[Edge]:
        return self.edges

    def get_nodes(self) -> Set[Node]:
        return self.nodes

    def get_components(self) -> List[int]:
        nr = 0
        nodes = self.get_nodes()
        comp = [-1] * len(nodes)

        for node in nodes:
            if comp[node.get_id()] == -1:
                nr = nr + 1
                comp[node.get_id()] = nr
                Graph.components_recursive_helper(nr, node.get_id(), self, comp)
        return comp

    def draw(self, file_name: str = "graph.png") -> None:
        Drawer.draw(self, file_name)

    def randomize(self, number_of_randomization: int) -> None:
        for i in range(number_of_randomization):
            edges = self.get_edges()
            random_edges: List[Edge] = random.sample(edges, 2)

            while True:
                break_outer = False
                first_edge_ids = random_edges[0].get_nodes_ids()
                second_edge_ids = random_edges[1].get_nodes_ids()
                for node in first_edge_ids:
                    if node in second_edge_ids:
                        random_edges: List[Edge] = random.sample(edges, 2)
                        break_outer = False
                        break
                    else:
                        break_outer = True
                if break_outer:
                    final_check = False
                    for edge in edges:
                        edge_nodes = edge.get_nodes_ids()
                        if (edge_nodes[0].get_id() == first_edge_ids[0].get_id() and edge_nodes[1].get_id() ==
                                second_edge_ids[1].get_id() or
                                edge_nodes[0].get_id() == second_edge_ids[1].get_id() and edge_nodes[1].get_id() ==
                                first_edge_ids[0].get_id() or
                                edge_nodes[0].get_id() == first_edge_ids[1].get_id() and edge_nodes[1].get_id() ==
                                second_edge_ids[0].get_id() or
                                edge_nodes[0].get_id() == second_edge_ids[0].get_id() and edge_nodes[1].get_id() ==
                                first_edge_ids[1].get_id()):
                            final_check = True
                            break
                    if final_check is False:
                        break
                    random_edges: List[Edge] = random.sample(edges, 2)

            self.remove_edge(random_edges[0])
            self.remove_edge(random_edges[1])

            first_edge_ids = random_edges[0].get_nodes_ids()
            second_edge_ids = random_edges[1].get_nodes_ids()

            self.add_edge(first_edge_ids[0], second_edge_ids[1])
            self.add_edge(first_edge_ids[1], second_edge_ids[0])

    def get_node_level(self, node: int) -> int:
        node_level = 0
        edges = self.get_edges()

        for e in edges:
            nodes_of_edge = e.get_nodes_ids()
            if nodes_of_edge[0].get_id() == node or nodes_of_edge[1].get_id() == node:
                node_level += 1

        return node_level

    def get_nodes_levels(self) -> List[int]:
        nodes_level = [0] * len(self.get_nodes())
        edges = self.get_edges()
        for e in edges:
            nodes_of_edge = e.get_nodes_ids()
            nodes_level[nodes_of_edge[0].get_id()] += 1
            nodes_level[nodes_of_edge[1].get_id()] += 1

        return nodes_level

    def is_consistent(self) -> bool:
        nodes_level = self.get_nodes_levels()
        return len(list(filter(lambda x: x == 0, nodes_level))) == 0

    def is_k_regular(self, k: int) -> bool:
        nodes_level = self.get_nodes_levels()
        return self.is_consistent() and len(list(filter(lambda x: x != k, nodes_level))) == 0

    def is_euler(self) -> bool:
        nodes_level = self.get_nodes_levels()

        return self.is_consistent() and len(list(filter(lambda x: x > 0 and x % 2 == 1, nodes_level))) == 0

    def is_hamilton(self) -> bool:
        if self.is_consistent() is False:
            return False

        return True
