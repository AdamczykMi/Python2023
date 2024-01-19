import unittest
from project import Graph, graph_coloring, is_safe


class TestGraphFunctionality(unittest.TestCase):

    def test_add_edge(self):
        graph = Graph(4)
        graph.add_edge(0, 1)
        self.assertIn(1, graph.graph[0])
        self.assertIn(0, graph.graph[1])

    def test_generate_random_edges(self):
        graph = Graph(4)
        graph.generate_random_edges(0.5)
        total_edges = sum(len(v) for v in graph.graph) // 2
        self.assertGreaterEqual(total_edges, 1)

    def test_is_safe(self):
        graph = Graph(3)
        graph.add_edge(0, 1)
        color = [1, 2, 0]
        self.assertTrue(is_safe(2, color, graph.graph, 1))

    def test_graph_coloring(self):
        graph = Graph(3)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        color = [0] * 3
        self.assertTrue(graph_coloring(graph, 3, color, 0))
        self.assertNotEqual(color, [0] * 3)


if __name__ == '__main__':
    unittest.main()
