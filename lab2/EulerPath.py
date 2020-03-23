from lab1.GraphGeneratorNL import GraphGeneratorNL
from lab1.Representations import adjacency_list


def eulerPath(graph):
    path = set()
    adj_list = adjacency_list(graph)
    edges = list(graph.edges)
    print(edges)
    DFSeuler(adj_list, edges,path)
    return path

def DFSeuler(adj_list, edges,path):
    for v in adj_list:
        for u in adj_list[v]:
            to_del = (v, u)
            edges.remove(to_del)
            DFSeuler(adj_list, edges,path)
        path.add(v)



n = 10
l = 7
G = GraphGeneratorNL(n, l)
eul  = eulerPath(G)
print(eul)
