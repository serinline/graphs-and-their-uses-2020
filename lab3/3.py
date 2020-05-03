from graphlib.algorithms.Algorithms import Algorithms
from graphlib.Generator import graph_generator_consistent_weighted

g = graph_generator_consistent_weighted(7, 1, 10)
g.draw("graph_weighted.png")

nodes = g.get_nodes()
nodes_len = len(nodes)

distances = [[0 for x in range(nodes_len)] for y in range(nodes_len)]

for i in range(nodes_len):
    for j in range(nodes_len):
        if i >= j:
            continue
        distance, path = Algorithms.dijkstra(g, i, j)
        distances[i][j] = distance
        distances[j][i] = distance

print("\n".join(["".join(["{:4}".format(item) for item in row])
                 for row in distances]))
