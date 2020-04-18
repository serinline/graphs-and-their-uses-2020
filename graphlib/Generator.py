from itertools import combinations
from random import random, sample

from graphlib.Graph import Graph


def graph_generator_nl(n: int, l: int) -> Graph:
    vertices = set([v for v in range(n)])
    e = set()

    comb = combinations(vertices, 2)
    random_comb = sample(list(comb), l)
    for c in random_comb:
        e.add(c)

    graph = Graph()
    graph.add_edges_from(e)

    return graph


def graph_generator_np(n: int, p: float) -> Graph:
    vertices = set([v for v in range(n)])
    e = set()

    for c in combinations(vertices, 2):
        tmp = random()
        if tmp < p:
            e.add(c)

    graph = Graph()
    graph.add_edges_from(e)

    return graph
