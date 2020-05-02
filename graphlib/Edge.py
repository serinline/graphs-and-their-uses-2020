from graphlib.Node import Node


class Edge:
    """
    Class representing single graph Edge
    """
    nodes: tuple
    directed: bool
    visited: bool
    weight: int

    def __init__(self, first_node: Node, second_node: Node, directed: bool = False, visited: bool = False, weight: int = 1) -> None:
        self.nodes = (first_node, second_node)
        self.directed = directed
        self.visited = visited
        self.weight = weight

    def __str__(self) -> str:
        return f"Edge (from: ${self.nodes[0]} to: ${self.nodes[1]})"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other) -> bool:
        return self.nodes == other.nodes

    def set_nodes_id_single(self, first_node: Node, second_node: Node) -> None:
        self.nodes = (first_node, second_node)

    def set_nodes_ids(self, nodes: tuple) -> None:
        self.nodes = nodes

    def get_nodes_ids(self) -> tuple:
        return self.nodes

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight
