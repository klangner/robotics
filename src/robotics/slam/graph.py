'''
Created on 24-05-2013

@author: Krzysztof Langner
'''

import networkx as nx


class GraphConverter():

    def create_graph(self, world_map):
        
        self.graph =  nx.DiGraph()
        self.row_count = len(world_map[0])
        self.column_count = len(world_map)
        # Add nodes
        for i in range(len(world_map)):
            row = world_map[i]
            for j in range(len(row)):
                if world_map[i][j] > 0:
                    self.graph.add_node(self._to_index(i, j), col=i, row=j)
        # Add vertices
        for i in range(len(world_map)):
            row = world_map[i]
            for j in range(len(row)):
                if world_map[i][j] > 0:
                    src_node = self._to_index(i, j)
                    self._add_edge(src_node, i-1, j-1)
                    self._add_edge(src_node, i-1, j)
                    self._add_edge(src_node, i-1, j+1)
                    self._add_edge(src_node, i, j-1)
                    self._add_edge(src_node, i, j+1)
                    self._add_edge(src_node, i+1, j-1)
                    self._add_edge(src_node, i+1, j)
                    self._add_edge(src_node, i+1, j+1)
        return self.graph
    
    def _to_index(self, column, row):
        return row*self.column_count + column

    def _add_edge(self, src_node, column, row):
        if column >= 0 and column < self.column_count and row >= 0 and row < self.row_count:
            dest = self._to_index(column, row)
            if dest in self.graph.node:
                self.graph.add_edge(src_node, dest)
