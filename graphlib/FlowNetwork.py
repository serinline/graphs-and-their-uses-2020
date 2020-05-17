from graphlib.DirectedGraph import DirectedGraph
from graphlib.Graph import Graph
from typing import List, Set
from graphlib.Edge import Edge
from graphlib.Node import Node

from graphlib.drawer.drawer import Drawer

class FlowNetwork(DirectedGraph):
    layers : Set[int]

    def __init__(self, edges: List[Edge] = None, nodes: Set[Node] = None, is_weighted = False):
        DirectedGraph.__init__(self, edges, nodes, is_weighted)
        self.layers = list()


    def get_layers(self) -> Set[int]:
        return self.layers


    def add_layer(self, layer : Set[int]) -> None:
        self.layers.append(layer)

    
    def draw(self, file_name: str = "graph.png") -> None:
        Drawer.draw_flow_network(self, file_name)

    

