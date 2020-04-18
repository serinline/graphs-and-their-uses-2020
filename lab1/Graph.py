class Graph:

    edges = []
    nodes = set()

    def add_edge(self, node, neighbour):
        self.nodes.add(node)
        self.nodes.add(neighbour)
        if node not in self.edges:
            self.edges.append((node, neighbour))
        else:
            self.edges[node].append(neighbour)

    def add_edges_from(self, nodes_set):
        for edge in nodes_set:
            self.add_edge(edge[0], edge[1])

    def print_edges(self):
        for node in self.edges:
            for neighbour in self.edges[node]:
                print("(", node, ", ", neighbour, ")")



G = Graph()
G.add_edges_from(((2,3), (2,4), (1,2)))
print(G.edges)