import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import tkinter as tk
from project import Graph, GUIApp

class TestGraphApp(unittest.TestCase):
    def setUp(self):
        self.graph_app = GUIApp(tk.Tk())

    @patch('sys.stdout', new_callable=StringIO)
    def test_generate_graph_with_valid_input(self, mock_stdout):
        with patch.object(tk.messagebox, 'showerror'):
            self.graph_app.total_vertices_entry.insert(0, "5")
            self.graph_app.generate_graph()
            self.assertEqual(mock_stdout.getvalue().strip(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_generate_graph_with_invalid_input(self, mock_stdout):
        with patch.object(tk.messagebox, 'showerror') as mock_showerror:
            self.graph_app.generate_graph()
            mock_showerror.assert_called_once_with("Błąd",
                                                   "Proszę wpisać liczbę wierzchołków przed generowaniem grafu.")
            self.assertEqual(mock_stdout.getvalue().strip(), "")

    def test_generate_random_graph(self):
        graph = Graph()
        graph.generate_random_graph(5, probability=0.4)
        self.assertEqual(len(graph.graph.nodes), 5)
        self.assertEqual(len(graph.colors), 5)
        self.assertEqual(graph.colors[0], 0)

    def test_color_graph(self):
        graph = Graph()
        graph.generate_random_graph(5, probability=0.4)
        graph.color_graph()
        self.assertTrue(all(color >= 0 for color in graph.colors))
        self.assertTrue(all(color < 5 for color in graph.colors))

    @patch.object(Graph, 'draw_colored_graph')
    def test_generate_graph_calls_draw_colored_graph(self, mock_draw_colored_graph):
        self.graph_app.total_vertices_entry.insert(0, "5")
        self.graph_app.generate_graph()
        mock_draw_colored_graph.assert_called_once()


if __name__ == '__main__':
    unittest.main()
