from typing import List

from graphlib.algorithms.Algorithms import Algorithms

from graphlib.Graph import Graph
from graphlib.representations.AdjacencyList import AdjacencyList


def check_degree(input_list: List[int]) -> None:
    if Algorithms.is_degree_sequence(input_list):
        print("Input is graphic sequence")
        g = Graph().create_graph_from_graphic_sequence(input_list)
        AdjacencyList(g).print()
        g.randomize(100)
        print("Randomized")
        AdjacencyList(g).print()
    else:
        print("Input is not graphic sequence")


input_is_degree = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
input_is_not_degree = [4, 4, 3, 1, 2]

print(input_is_degree)
check_degree(input_is_degree)

print(input_is_not_degree)
check_degree(input_is_not_degree)
