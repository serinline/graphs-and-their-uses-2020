from typing import Dict

from graphlib.Graph import Graph


class AdjencyList:
    list: Dict

    def __init__(self, graph: Graph) -> None:
        self.list = {key: [] for key in range(len(graph.get_nodes()))}

        for edge in graph.get_edges():
            nodes = edge.get_nodes_ids()
            self.list[nodes[0]].append(nodes[1])

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return str(self.list)

    def print(self) -> None:
        print(self.list)
