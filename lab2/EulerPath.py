from lab1.GraphGeneratorNL import GraphGeneratorNL

def eulerPath(graph):

    path = []
    visited = set()
    stack = []

    while stack:
        for edge in graph.edges():
            if edge not in visited:
                visited.add(edge)
            break

    return path


n = 10
l = 7
G = GraphGeneratorNL(n, l)
eulerPath(G)
