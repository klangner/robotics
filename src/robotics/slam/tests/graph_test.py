'''
Created on 24-05-2013

@author: Krzysztof Langner
'''
import unittest
from robotics.slam.graph import GraphConverter


class GraphTest(unittest.TestCase):


    def testCreateGraph(self):
        world = [[1, 1], [1, 1]]
        converter = GraphConverter()
        graph = converter.create_graph(world)
        self.assertEqual(4, len(graph.nodes()))
        self.assertEqual(12, len(graph.edges()))


    def testCreateGraph2(self):
        world = [[1, 0], [1, 1]]
        converter = GraphConverter()
        graph = converter.create_graph(world)
        self.assertEqual(3, len(graph.nodes()))
        self.assertEqual(6, len(graph.edges()))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()