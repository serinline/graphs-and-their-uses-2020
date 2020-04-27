from itertools import groupby
from operator import itemgetter

from graphlib.Graph import Graph

input_is_degree = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2, 1, 1]
g = Graph().create_graph_from_graphic_sequence(input_is_degree)

components = g.get_components()
groups = groupby(enumerate(components), itemgetter(1))

for (key, data) in groups:
    print(f"Component({key}): ", end="")
    for item in data:
        print(item[0], end=", ")
    print()
