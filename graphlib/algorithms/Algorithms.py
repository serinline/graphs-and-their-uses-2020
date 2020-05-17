import math

import numpy as np

from typing import List
from queue import PriorityQueue

from graphlib.DirectedGraph import DirectedGraph
from graphlib.Edge import Edge
from graphlib.Node import Node
from graphlib.representations.AdjacencyList import AdjacencyList
from graphlib.representations.AdjacencyMatrix import AdjacencyMatrix
import copy

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
        neighbours = graph.find_directed_neighbours(v, graph)
        for u in neighbours:
            if d[u] == -1:
                t = cls.DFS_visit(u, graph, d, f, t)
        t += 1
        f[v] = t
        return t

    @classmethod
    def components_r(cls, nr, v, graph_T, comp):
        neighbours = graph_T.find_directed_neighbours(v, graph_T)
        for u in neighbours:
            if comp[u] == -1:
                comp[u] = nr
                cls.components_r(nr, v, graph_T, comp)

    @classmethod
    def init(cls, graph, start) -> (List[int], List[int]):
        n = len(graph.get_nodes())
        d_s = [math.inf for i in range(n)]
        p_s = [None for i in range(n)]
        d_s[start] = 0
        return d_s, p_s

    @classmethod
    def bellman_ford(cls, graph, start=0) -> (bool, List[int]):
        n = len(graph.get_nodes())
        d_s, p_s = cls.init(graph, start)
        for i in range(1, n - 1):
            for edge in graph.get_edges():
                nodes = edge.get_nodes_ids()
                u = nodes[0].get_id()
                v = nodes[1].get_id()
                w = edge.get_weight()
                if d_s[v] > (d_s[u] + w):
                    d_s[v] = d_s[u] + w
                    p_s[v] = u
        for edge in graph.get_edges():
            nodes = edge.get_nodes_ids()
            u = nodes[0].get_id()
            v = nodes[1].get_id()
            w = edge.get_weight()
            if d_s[v] > (d_s[u] + w):
                return False, d_s
        return True, d_s

    @classmethod
    def johnson(cls, graph) -> List[List[int]] or None:

        new_graph = Algorithms.add_s(graph)
        nodes = [i.get_id() for i in new_graph.get_nodes()]
        added_node = nodes[len(nodes) - 1]
        val, d_s = cls.bellman_ford(new_graph, added_node)

        if not val:
            raise Exception("ERROR")

        h = [0 for i in range(len(nodes))]
        for v in nodes:
            h[v] = d_s[v]
        for edge in new_graph.get_edges():
            nodes = edge.get_nodes_ids()
            u = nodes[0].get_id()
            v = nodes[1].get_id()
            w = edge.get_weight()
            edge.set_weight(w + h[u] - h[v])

        cls.copy_weights(new_graph, graph)

        D = [[0 for x in range(len(graph.get_nodes()))] for y in range(len(graph.get_nodes()))]
        old_nodes = [i.get_id() for i in graph.get_nodes()]
        for u in old_nodes:
            for v in old_nodes:
                dist, path = cls.dijkstra_directed(graph, u, v)
                D[u][v] = dist - h[u] + h[v]
        return D

    @classmethod
    def add_s(cls, graph) -> DirectedGraph:
        graph_copy = graph.copy()
        s = Node(len(graph.get_nodes()))
        for i in range(len(graph.get_nodes())):
            graph_copy.add_weighted_edge(s, Node(i), weight=0)

        return graph_copy

    @classmethod
    def copy_weights(cls, graph_src, graph_to) -> None:
        for edge in graph_src.get_edges():
            nodes = edge.get_nodes_ids()
            u = nodes[0].get_id()
            v = nodes[1].get_id()
            w = edge.get_weight()
            try:
                edge_to = graph_to.find_directed_edge(u, v)
                edge_to.set_weight(w)
            except:
                pass

    @classmethod
    def dijkstra_directed(cls, graph, from_node_id: int, to_node_id: int):
        nodes = graph.get_nodes()

        d = [math.inf] * len(nodes)
        d[from_node_id] = 0
        p = [False] * len(nodes)

        Q = PriorityQueue()
        for i, v in enumerate(d):
            Q.put((v, i))

        while Q.empty() is False:
            _, n_id = Q.get()
            for neighbour in graph.find_neighbours(n_id, graph):
                try:
                    edge = graph.find_directed_edge(n_id, neighbour)
                    if d[neighbour] > d[n_id] + edge.get_weight():
                        d[neighbour] = d[n_id] + edge.get_weight()
                        p[neighbour] = n_id
                        new_Q = PriorityQueue()
                        for v, i in Q.queue:
                            if i == neighbour:
                                v = d[n_id] + edge.get_weight()
                            new_Q.put((v, i))
                        Q = new_Q
                except:
                    pass

        path = [to_node_id]
        x = p[to_node_id]
        while x is not False:
            path.append(x)
            x = p[x]

        path.reverse()

        return d[to_node_id], path

    @classmethod
    def dijkstra(cls, graph, from_node_id: int, to_node_id: int):
        nodes = graph.get_nodes()

        d = [math.inf] * len(nodes)
        d[from_node_id] = 0
        p = [False] * len(nodes)

        Q = PriorityQueue()
        for i, v in enumerate(d):
            Q.put((v, i))

        while Q.empty() is False:
            _, n_id = Q.get()
            for neighbour in graph.find_neighbours(n_id, graph):
                edge = graph.find_edge(n_id, neighbour)
                if d[neighbour] > d[n_id] + edge.get_weight():
                    d[neighbour] = d[n_id] + edge.get_weight()
                    p[neighbour] = n_id
                    new_Q = PriorityQueue()
                    for v, i in Q.queue:
                        if i == neighbour:
                            v = d[n_id] + edge.get_weight()
                        new_Q.put((v, i))
                    Q = new_Q

        path = [to_node_id]
        x = p[to_node_id]
        while x is not False:
            path.append(x)
            x = p[x]

        path.reverse()

        return d[to_node_id], path

    @classmethod
    def get_graph_center(cls, graph):
        nodes = graph.get_nodes()
        nodes_len = len(nodes)

        distances = [[0 for x in range(nodes_len)] for y in range(nodes_len)]

        for i in range(nodes_len):
            for j in range(nodes_len):
                if i >= j:
                    continue
                distance, path = Algorithms.dijkstra(graph, i, j)
                distances[i][j] = distance
                distances[j][i] = distance
        sum_arr = [0] * nodes_len
        for i in range(nodes_len):
            sum_arr[i] = np.sum(distances[i])
        return sum_arr.index(min(sum_arr))

    @classmethod
    def get_graph_center_minimax(cls, graph):
        nodes = graph.get_nodes()
        nodes_len = len(nodes)

        distances = [[0 for x in range(nodes_len)] for y in range(nodes_len)]

        for i in range(nodes_len):
            for j in range(nodes_len):
                if i >= j:
                    continue
                distance, path = Algorithms.dijkstra(graph, i, j)
                distances[i][j] = distance
                distances[j][i] = distance

        max_arr = [0] * nodes_len
        for i in range(nodes_len):
            max_arr[i] = max(distances[i])
        return max_arr.index(min(max_arr))

    @classmethod
    def prim(cls, graph):
        nodes = graph.get_nodes()
        edges = []

        W = list(range(len(nodes)))
        W.remove(0)
        T = [0]

        while len(T) != len(nodes):
            interesting_edges = []
            for node_id in T:
                for node_2_id in W:
                    edge = graph.find_edge(node_id, node_2_id)
                    if edge is not None:
                        interesting_edges.append(edge)
            interesting_edges.sort(key=lambda e: e.get_weight())
            edges.append(interesting_edges[0])
            nodes_of_edge = interesting_edges[0].get_nodes_ids()
            node_1_id = nodes_of_edge[0].get_id()
            node_2_id = nodes_of_edge[1].get_id()
            if node_1_id in T:
                T.append(node_2_id)
                W.remove(node_2_id)
            else:
                T.append(node_1_id)
                W.remove(node_1_id)

        return edges

    @classmethod
    def breadth_first_search(cls, graph, s):
        ps = list([])
        ds = list()
        for v in graph.get_nodes():
            ps.append(list([None]))
            ds.append(math.inf)
        ds[s] = 0

        queue = list()
        queue.append(Node(s))
        
        while(len(queue)):
            v = queue.pop(0)
            neighbours = list([])
            for e in graph.get_edges():
                if e.get_nodes_ids()[0] == v :
                    if graph.find_edge(e.get_nodes_ids()[0].get_id(), e.get_nodes_ids()[1].get_id()).get_capacity() != 0:
                        neighbours.append(e.get_nodes_ids()[1])
            for u in neighbours:
                if ds[u.get_id()] == math.inf:
                    ds[u.get_id()] = ds[v.get_id()]+1
                    ps[u.get_id()] = v
                    queue.append(u)
        
        if(ds[-1] == math.inf):
            return None

        # print(ps)
        # print(ds)

        l = list()
        layers = graph.get_layers()
        l.append( Node(layers[-1][0]) )
        l.append( ps[-1] )
        while not(l[-1] == Node(s)):
            l.append(ps[l[-1].get_id()])

        return l


    @classmethod
    def ford_fulkerson(cls, graph, s, t):
        while(True):
            gf = copy.deepcopy(graph)
            gf.clear_edges()
            e = list()
            for i in graph.get_nodes():
                for j in graph.get_nodes():
                    if(i == j):
                        continue
                    if graph.is_edge_in_graph( i.get_id(), j.get_id() ):
                        e.append(Edge(i, j))
                        edge = graph.find_edge(i.get_id(), j.get_id())
                        e[-1].set_capacity(edge.get_capacity() - edge.get_flow())

                    elif graph.is_edge_in_graph( j.get_id(), i.get_id() ):
                        e.append(Edge(i, j))
                        edge = graph.find_edge(i.get_id(), j.get_id())
                        e[-1].set_capacity(edge.get_flow())
                        
                    else:
                        e.append(Edge(i, j))
                        e[-1].set_capacity(0)

            gf.add_edges(e)
            
            nodes = cls.breadth_first_search(gf, s)
            if nodes == False or nodes == [None] or nodes == None:
                break
            
            # print(nodes)

            edges = list()
            for i in range(0, len(nodes)-1):
                edges.append(gf.find_edge(nodes[i+1].get_id(), nodes[i].get_id()))

            cf = edges[0].get_capacity()
            for e in edges:
                if e.get_capacity() < cf:
                    cf = e.get_capacity()

            # print(cf)

            for e in edges:
                if graph.is_edge_in_graph(e.get_nodes_ids()[0].get_id(), e.get_nodes_ids()[1].get_id()):
                    x = e.get_nodes_ids()[0].get_id()
                    y = e.get_nodes_ids()[1].get_id()
                    graph.find_edge(x, y).set_flow(graph.find_edge(x, y).get_flow()+cf)
                    
                elif graph.is_edge_in_graph(e.get_nodes_ids()[1].get_id(), e.get_nodes_ids()[0].get_id()):
                    x = e.get_nodes_ids()[0].get_id()
                    y = e.get_nodes_ids()[1].get_id()
                    graph.find_edge(y, x).set_flow(graph.find_edge(y, x).get_flow()-cf)

        res = 0
        for e in graph.get_edges():
            if e.get_nodes_ids()[1].get_id() == t:
                res += e.get_flow()

        return res
        