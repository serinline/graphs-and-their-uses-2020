from typing import Dict

from graphlib.Graph import Graph


class AdjacencyList:
    list: Dict

    def __init__(self, graph: Graph) -> None:
        self.list = {key: [] for key in range(len(graph.get_nodes()))}

        for edge in graph.get_edges():
            nodes = edge.get_nodes_ids()
            self.list[nodes[0].get_id()].append(nodes[1].get_id())
            self.list[nodes[1].get_id()].append(nodes[0].get_id())

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return str(self.list)

    def get_list(self) -> Dict:
        return self.list

    def print(self) -> None:
        print(self.list)
