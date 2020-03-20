import numpy
from GraphGeneratorNL import GraphGeneratorNL as gr

#here is a bug, index out of range but idk why ><
def adjacency_list(graph):
    adj_list = list()
    for edge in graph.edges():
        adj_list[edge[0]].append(edge[1])
        

n = 10
l = 7
G = gr(n, l)
print(adjacency_list(G))
