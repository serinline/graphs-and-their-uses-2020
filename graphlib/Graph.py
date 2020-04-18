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

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"Graph(\n\tNodes=[${self.nodes}]\n\tEdges=[${self.edges}]\n)"

    def __eq__(self, other) -> bool:
        return self.edges == other.edges and self.nodes == other.nodes

    def add_edge(self, first_node: Node, second_node: Node) -> None:
        self.nodes.add(first_node)
        self.nodes.add(second_node)

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
