import math

import numpy as np

from typing import List

from graphlib.DirectedGraph import DirectedGraph
from graphlib.Edge import Edge
from graphlib.Node import Node
from graphlib.representations.AdjacencyList import AdjacencyList
from graphlib.representations.AdjacencyMatrix import AdjacencyMatrix


class Algorithms:
    @classmethod
    def is_degree_sequence(cls, sequence_input: List[int]) -> bool:
        if len(list(filter(lambda x: x % 2 == 1, sequence_input))) % 2 == 1:
            return False

        sequence = sequence_input[:]
        n = len(sequence)
        sequence.sort(reverse=True)
        while True:
            if all(v == 0 for v in sequence):
                return True

            if sequence[0] < 0 or sequence[0] >= n or np.sum(sequence) < 0:
                return False

            i = 1
            while i <= sequence[0]:
                sequence[i] = sequence[i] - 1
                i = i + 1

            sequence[0] = 0
            sequence.sort(reverse=True)

    @classmethod
    def euler_cycle(cls, graph) -> List[int]:
        cycle = []
        adj_matrix = AdjacencyMatrix(graph).get_matrix()

        def dfs_euler(v):
            for u in range(len(graph.get_nodes())):
                if adj_matrix[v][u] > 0:
                    adj_matrix[v][u] -= 1
                    adj_matrix[u][v] -= 1
                    dfs_euler(u)
            cycle.append(v)

        nodes = range(len(graph.get_nodes()))
        dfs_euler(nodes[0])

        return cycle

    @classmethod
    def hamilton_cycle(cls, graph, v=0, cycle=None) -> List[int] or None:
        if cycle is None:
            cycle = []
        adj_list = AdjacencyList(graph).get_list()
        size = len(adj_list)

        if v not in set(cycle):
            cycle.append(v)

            if len(cycle) == size:
                if cycle[-1] in adj_list[cycle[0]]:
                    cycle.append(cycle[0])
                    return cycle
                else:
                    cycle.pop()
                    return None

            for v_next in adj_list.get(v, []):
                cycle_cp = cycle[:]
                hamilton_candidate = cls.hamilton_cycle(graph, v_next, cycle_cp)
                if hamilton_candidate is not None:
                    return hamilton_candidate

    @classmethod
    def kosaraju(cls, graph) -> List[int] or None:
        vertices = graph.get_nodes()
        v_nodes = [n.get_id() for n in vertices]
        n = len(vertices)
        d = [-1 for i in range(n)]
        f = [-1 for i in range(n)]
        t = 0
        for v in v_nodes:
            if d[v] == -1:
                t = cls.DFS_visit(v, graph, d, f, t)
        graph_T = graph.transponse(graph)
        nr = 0
        comp = [-1 for i in range(n)]
        f = [(key, val) for key, val in enumerate(f, 0)]
        f.sort(key=lambda val: val[1], reverse=True)
        for vert in f:
            v = vert[0]
            if comp[v] == -1:
                nr += 1
                comp[v] = nr
                cls.components_r(nr, v, graph_T, comp)
        return comp

    @classmethod
    def DFS_visit(cls, v, graph, d, f, t):
        t += 1
        d[v] = t
        neighbours = graph.find_neighbours(v, graph)
        for u in neighbours:
            if d[u] == -1:
                t = cls.DFS_visit(u, graph, d, f, t)
        t += 1
        f[v] = t
        return t

    @classmethod
    def components_r(cls, nr, v, graph_T, comp):
        neighbours = graph_T.find_neighbours(v, graph_T)
        for u in neighbours:
            if comp[u] == -1:
                comp[u] = nr
                cls.components_r(nr, v, graph_T, comp)

    @classmethod
    def init(cls, graph):
        n = len(graph.get_nodes())
        d_s = [math.inf for i in range(n)]
        p_s = [0 for i in range(n)]
        return d_s, p_s

    @classmethod
    def bellman_ford(cls, graph, start=0) -> bool:
        n = len(graph.get_nodes())
        d_s, p_s = cls.init(graph)
        d_s[start] = 0
        for i in range(n - 1):
            for edge in graph.get_edges():
                nodes = edge.get_nodes_ids()
                u = nodes[0]
                v = nodes[1]
                w = edge.get_weight()
                cls.relax(u, v, w, d_s, p_s)
            for edge in graph.get_edges():
                nodes = edge.get_nodes_ids()
                u = nodes[0]
                v = nodes[1]
                w = edge.get_weight()
                if d_s[v.get_id()] > d_s[u.get_id()] + w:
                    return False, d_s
        return True, d_s

    @classmethod
    def relax(cls, u, v, w, d_s, p_s):
        if d_s[v.get_id()] > d_s[u.get_id()] + w:
            d_s[v.get_id()] = d_s[u.get_id()] + w
            p_s[v.get_id()] = u

    @classmethod
    def johnson(cls, graph) -> List[List[int]] or None:
        new_graph = cls.add_s(graph)
        nodes = new_graph.get_nodes()
        added_node = nodes.pop()
        val, d_s = cls.bellman_ford(new_graph, added_node.get_id())
        if not val:
            raise Exception("ERROR")
        h = [0 for i in range(len(nodes))]
        for v in nodes:
            h[v.get_id()] = d_s[v.get_id()]
        for edge in new_graph.get_edges():
            nodes = edge.get_nodes_ids()
            u = nodes[0]
            v = nodes[1]
            edge.set_weight(edge.get_weight() + h[u] - h[v])
        D = [[] for i in range(len(graph.get_nodes()))]

        old_nodes = graph.get_nodes()
        for u in old_nodes:
            # d_u = dijkstra(graph, u)
            for v in old_nodes:
                pass
                # D[u.get_id()][v.get_id()] = d_u[v.get_id()] - h[u.get_id()] + h[v.get_id()]
        return D


    @classmethod
    def add_s(cls, graph) -> DirectedGraph:
        graph_copy = graph.copy()
        s = Node(len(graph.get_nodes()))
        graph_copy.get_nodes().append(s)

        for node in graph_copy.get_nodes():
            graph_copy.get_edges().append(Edge(s, node, weight=0))

        return graph_copy
