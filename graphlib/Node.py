class Node:
    """
    Class representing single graph Node
    """
    id: int
    visited: bool

    def __init__(self, node_id: int = None, node_visited: bool = False) -> None:
        self.id = node_id
        self.visited = node_visited

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"Node(id: ${self.id} visited: ${self.visited})"

    def __eq__(self, other) -> bool:
        return self.id == other.id and self.visited == other.visited

    def set_id(self, node_id: int = None) -> None:
        self.id = node_id

    def set_visited(self, node_visited: bool = False) -> None:
        self.visited = node_visited

    def get_id(self) -> int:
        return self.id

    def get_visited(self) -> bool:
        return self.visited
