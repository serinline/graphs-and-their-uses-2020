from typing import List

from graphlib.Graph import Graph
from graphlib.DirectedGraph import DirectedGraph


class IncidenceMatrix:
    matrix: List[List[int]]

    def __init__(self, graph: Graph):
        self.matrix = []
        for i in range(len(graph.get_nodes())):
            self.matrix.append([0 for j in range(len(graph.get_edges()))])

        for edge_idx, edge in enumerate(graph.get_edges()):
            nodes_ids = edge.get_nodes_ids()
            self.matrix[nodes_ids[0].get_id()][edge_idx] = 1
            self.matrix[nodes_ids[1].get_id()][edge_idx] = 1

    def print(self):
        for i in self.matrix:
            print(i)


class DirectedIncidenceMatrix(IncidenceMatrix):
    def __init__(self, graph: DirectedGraph):
        self.matrix = []
        for i in range(len(graph.get_nodes())):
            self.matrix.append([0 for j in range(len(graph.get_edges()))])

        for edge_idx, edge in enumerate(graph.get_edges()):
            nodes_ids = edge.get_nodes_ids()
            self.matrix[nodes_ids[0].get_id()][edge_idx] = -1
            self.matrix[nodes_ids[1].get_id()][edge_idx] = 1
