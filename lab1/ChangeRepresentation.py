import numpy
from GraphGeneratorNL import GraphGeneratorNL as gr


def adjacency_list(graph):
    adj_list = {key: [] for key in range(len(graph.nodes))}

    for edge in graph.edges():
        #print(adj_list)
        adj_list[edge[0]].append(edge[1])
        
    return adj_list


n = 10
l = 7
G = gr(n, l)
print(adjacency_list(G))