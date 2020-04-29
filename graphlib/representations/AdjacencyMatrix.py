from typing import List

from graphlib.Graph import Graph
from graphlib.DirectedGraph import DirectedGraph


class AdjacencyMatrix:
    matrix: List[List[int]]

    def __init__(self, graph: Graph):
        self.matrix = []
        for i in range(len(graph.get_nodes())):
            self.matrix.append([0 for j in range(len(graph.get_nodes()))])

        for edge in graph.get_edges():
            nodes_ids = edge.get_nodes_ids()
            self.matrix[nodes_ids[0].get_id()][nodes_ids[1].get_id()] = 1
            self.matrix[nodes_ids[1].get_id()][nodes_ids[0].get_id()] = 1

    def __repr__(self):
        return self.matrix

    def __str__(self):
        return str(self)

    def get_matrix(self):
        return self.matrix

    def print(self):
        for i in self.matrix:
            print(i)


class DirectedAdjacencyMatrix(AdjacencyMatrix):
    def __init__(self, graph: DirectedGraph):
        self.matrix = []
        for i in range(len(graph.get_nodes())):
            self.matrix.append([0 for j in range(len(graph.get_nodes()))])

        for edge in graph.get_edges():
            nodes_ids = edge.get_nodes_ids()
            self.matrix[nodes_ids[0].get_id()][nodes_ids[1].get_id()] = 1
