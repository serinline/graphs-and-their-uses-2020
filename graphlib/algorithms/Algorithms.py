import numpy as np

from typing import List

from graphlib.representations.AdjacencyList import AdjacencyList
from graphlib.representations.AdjacencyMatrix import AdjacencyMatrix, DirectedAdjacencyMatrix


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
        adj_matrix = DirectedAdjacencyMatrix(graph).matrix
        n = len(adj_matrix)
        d = [-1 for i in range(n)]
        f = [-1 for i in range(n)]
        t = [0]
        for v in range(n):
            if d[v] == -1:
                cls.DFS_visit(v, adj_matrix, d, f, t)
        graph_T = np.array(adj_matrix).T
        nr = 0
        comp = [-1 for i in range(n)]
        for v in reversed(sorted(range(len(f)), key=lambda k: f[k])):
            if comp[v] == -1:
                nr += 1
                comp[v] = nr
                cls.components_r(nr, v, graph_T, comp)
        return comp

    @classmethod
    def DFS_visit(cls, v, graph, d, f, t):
        t[0] += 1
        d[v] = t[0]
        for u in range(len(graph)):
            if graph[v][u] == 1 and d[u] == -1:
                cls.DFS_visit(u, graph, d, f, t)
        t[0] += 1
        f[v] = t[0]

    @classmethod
    def components_r(cls, nr, v, graph_T, comp):
        for u in range(len(graph_T)):
            if graph_T[v][u] == 1 and comp[u] == -1:
                comp[u] = nr
                cls.components_r(nr, u, graph_T, comp)
