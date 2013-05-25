'''
Created on 24-05-2013

@author: Krzysztof Langner
'''
from robotics.slam.graph import GraphConverter
import networkx as nx;


def astar_path(world_map, start, dest):
    converter = GraphConverter()
    graph = converter.create_graph(world_map)
    nodes = nx.astar_path(graph, start, dest, heuristic)
    return nodes

def heuristic(a, b):
    (ax, ay) = a
    (bx, by) = b
    x = (ax-bx)**2
    y = (ay-by)**2
    return float(x+y)**.5
