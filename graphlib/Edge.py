from graphlib.Node import Node


class Edge:
    """
    Class representing single graph Edge
    """
    nodes: tuple
    directed: bool
    visited: bool
    weight: int
    flow : int
    capacity : int

    def __init__(self, first_node: Node, second_node: Node, directed: bool = False, visited: bool = False, weight: int = 1, flow: int = 0, capacity: int = 0) -> None:
        self.nodes = (first_node, second_node)
        self.directed = directed
        self.visited = visited
        self.weight = weight
        self.flow = flow
        self.capacity = capacity

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

    def set_flow(self, flow):
        self.flow = flow

    def set_capacity(self, capacity):
        self.capacity = capacity

    def get_weight(self):
        return self.weight

    def get_flow(self) ->int:
        return self.flow

    def get_capacity(self) -> int:
        return self.capacity
