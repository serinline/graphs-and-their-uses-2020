import numpy
from lab1.graph_generator_nl import graph_generator_nl as gr


def adjacency_list(graph):
    adj_list = {key: [] for key in range(len(graph.nodes))}

    for edge in graph.edges:
        #print(adj_list)
        print(edge)
        adj_list[edge[0]].append(edge[1])
    # for node in graph.edges:
    #     for neighbour in graph.edges[node]:
    #         if neighbour is not None:
    #             adj_list[node].append(neighbour)
        
    return adj_list


def adjacency_matrix(graph):
    adj_mx = []
    for i in range(len(graph.nodes)):
        adj_mx.append([0 for i in range(len(graph.nodes))])

    for edge in graph.edges:
        adj_mx[edge[0]][edge[1]] = 1
        adj_mx[edge[1]][edge[0]] = 1

    return adj_mx


def incidence_matrix(graph):
    ic_mx = []
    for i in range(len(graph.nodes)):
        ic_mx.append([0 for i in range(len(graph.nodes))])

    for edge in graph.edges:
        ic_mx[edge[0]][edge[1]] = 1

    return ic_mx



n = 10
l = 7
G = gr(n, l)
print(adjacency_list(G))

print()

n = 10
l = 7
G2 = gr(n, l)

mx = adjacency_matrix(G2)
for i in mx:
    print(i)

print()

n = 10
l = 7
G2 = gr(n, l)

ix = incidence_matrix(G2)
for i in ix:
    print(i)