from itertools import combinations
from random import random, sample, randint, randrange

from graphlib.DirectedGraph import DirectedGraph
from graphlib.FlowNetwork import FlowNetwork
from graphlib.Graph import Graph
from graphlib.Node import Node


def graph_generator_nl(n: int, l: int) -> Graph:
    vertices = set([v for v in range(n)])
    e = set()

    comb = combinations(vertices, 2)
    random_comb = sample(list(comb), l)
    for c in random_comb:
        e.add((Node(c[0]), Node(c[1])))

    graph = Graph()

    for v in vertices:
        graph.add_node(Node(v))

    graph.add_edges_from(e)

    return graph


def graph_generator_np(n: int, p: float) -> Graph:
    vertices = set([v for v in range(n)])
    e = set()

    for c in combinations(vertices, 2):
        tmp = random()
        if tmp < p:
            e.add((Node(c[0]), Node(c[1])))

    graph = Graph()

    for v in vertices:
        graph.add_node(Node(v))

    graph.add_edges_from(e)

    return graph


def graph_generator_consistent_weighted(n: int, w_min: int, w_max: int) -> Graph:
    vertices = set([v for v in range(n)])
    e = set()

    l_min = n

    if n == 2:
        l_min = 1

    l = randint(l_min, (n * (n - 1)) / 2)

    while True:
        comb = combinations(vertices, 2)
        random_comb = sample(list(comb), l)
        for c in random_comb:
            e.add((Node(c[0]), Node(c[1]), randint(w_min, w_max)))

        graph = Graph(is_weighted=True)

        for v in vertices:
            graph.add_node(Node(v))

        graph.add_edges_from(e)

        if graph.is_consistent():
            return graph


def directed_graph_generator_np(n: int, p: float) -> DirectedGraph:
    vertices = list([v for v in range(n)])
    e = list()

    for c in combinations(vertices, 2):
        tmp = random()
        if tmp < p:
            e.append((Node(c[0]), Node(c[1])))
        tmp2 = random()
        if tmp2 < p:
            e.append((Node(c[1]), Node(c[0])))

    graph = DirectedGraph()

    for v in vertices:
        graph.add_node(Node(v))

    graph.add_edges_from(e)

    return graph


def flow_network_generator( N : int ) -> FlowNetwork:
    layers = list([])
    layers.append(list([0]))

    counter = 1
    for i in range(0, N):
        layers.append(list())
        tmp = randrange(2,N+1)
        for j in range(0, tmp):
            layers[i+1].append(counter)
            counter+=1

    layers.append(list([counter]))

    fn = FlowNetwork()
    for l in layers:
        fn.add_layer(l)
        for i in l:
            fn.add_node(Node(i))

    print(fn.layers)

    e = list()
    for i in fn.layers[1]:
        e.append((Node(0), Node(i)))

    for i in range ( 1, len(fn.layers)-2 ):
        for j in range ( fn.layers[i][0], fn.layers[i][-1]+1 ):
            tmp = randrange(fn.layers[i+1][0], fn.layers[i+1][-1]+1)
            e.append((Node(j), Node(tmp)))

    fn.add_edges_from(e)
    e.clear()

    for i in range ( 2, len(fn.layers)-1 ):
        for j in range ( fn.layers[i][0], fn.layers[i][-1]+1 ):
            is_connected = False
            for x in fn.get_edges():
                nodes = x.get_nodes_ids()
                if(nodes[1].get_id() == j):
                    is_connected = True
                    break
                
            if not(is_connected):
                tmp = randrange(fn.layers[i-1][0], fn.layers[i-1][-1]+1)
                e.append((Node(tmp), Node(j)))

    for i in fn.layers[-2]:
        e.append((Node(i), Node(fn.layers[-1][0])))

    fn.add_edges_from(e)

    last_index = fn.layers[len(fn.layers)-1][0]
    for i in range(0, 2*N):
        while(True):
            tmp1 = randrange( 0, last_index )
            tmp2 = randrange( 1, last_index+1 )
            if not( tmp1 == tmp2 or fn.is_edge_in_graph(tmp1, tmp2) or fn.is_edge_in_graph(tmp2, tmp1) ):
                fn.add_edge( Node(tmp1), Node(tmp2) )
                break
                    
    for i in fn.get_edges():
        i.set_capacity( randrange(1, 11) )

    return fn
