from itertools import combinations
from random import random, sample, randint

from graphlib.DirectedGraph import DirectedGraph
from graphlib.Graph import Graph
from graphlib.Node import Node


def graph_generator_nl(n: int, l: int) -> Graph:
    vertices = set([v for v in range(n)])
    e = set()

    comb = combinations(vertices, 2)
    random_comb = sample(list(comb), l)
    for c in random_comb:
        e.add((Node(c[0]), Node(c[1])))

    graph = Graph()

    for v in vertices:
        graph.add_node(Node(v))

    graph.add_edges_from(e)

    return graph


def graph_generator_np(n: int, p: float) -> Graph:
    vertices = set([v for v in range(n)])
    e = set()

    for c in combinations(vertices, 2):
        tmp = random()
        if tmp < p:
            e.add((Node(c[0]), Node(c[1])))

    graph = Graph()

    for v in vertices:
        graph.add_node(Node(v))

    graph.add_edges_from(e)

    return graph


def graph_generator_consistent_weighted(n: int, w_min: int, w_max: int) -> Graph:
    vertices = set([v for v in range(n)])
    e = set()

    l_min = n

    if n == 2:
        l_min = 1

    l = randint(l_min, (n * (n - 1)) / 2)

    while True:
        comb = combinations(vertices, 2)
        random_comb = sample(list(comb), l)
        for c in random_comb:
            e.add((Node(c[0]), Node(c[1]), randint(w_min, w_max)))

        graph = Graph(is_weighted=True)

        for v in vertices:
            graph.add_node(Node(v))

        graph.add_edges_from(e)

        if graph.is_consistent():
            return graph


def directed_graph_generator_np(n: int, p: float) -> DirectedGraph:
    vertices = list([v for v in range(n)])
    e = list()

    for c in combinations(vertices, 2):
        tmp = random()
        if tmp < p:
            e.append((Node(c[0]), Node(c[1])))
        tmp2 = random()
        if tmp2 < p:
            e.append((Node(c[1]), Node(c[0])))

    graph = DirectedGraph()

    for v in vertices:
        graph.add_node(Node(v))

    graph.add_edges_from(e)

    return graph

