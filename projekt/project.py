import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx
import random


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def generate_random_edges(self, density):
        # Dodaj losowe krawędzie do grafu na podstawie zadanej gęstości
        max_edges = (self.vertices * (self.vertices - 1)) // 2
        num_edges = int(density * max_edges)

        edges_added = 0
        while edges_added < num_edges:
            u = random.randint(0, self.vertices - 1)
            v = random.randint(0, self.vertices - 1)

            if u != v and v not in self.graph[u]:
                self.add_edge(u, v)
                edges_added += 1


def is_safe(vertex, color, graph, c):
    for neighbor in graph[vertex]:
        if color[neighbor] == c:
            return False
    return True


def graph_coloring(graph, m, color, v):
    if v == graph.vertices:
        return True

    for c in range(1, m + 1):
        if is_safe(v, color, graph.graph, c):
            color[v] = c
            if graph_coloring(graph, m, color, v + 1):
                return True
            color[v] = 0
    return False


class GraphInterface:
    def __init__(self, window):
        self.window = window
        self.window.title("Kolorowanie Grafu")

        # Tworzenie interfejsu
        tk.Label(window, text="Liczba wierzchołków:").pack()
        self.vertices_entry = tk.Entry(window)
        self.vertices_entry.pack()

        tk.Label(window, text="Liczba kolorów:").pack()
        self.colors_entry = tk.Entry(window)
        self.colors_entry.pack()

        tk.Label(window, text="Gęstość krawędzi (0-1):").pack()
        self.density_entry = tk.Entry(window)
        self.density_entry.pack()

        generate_button = tk.Button(window, text="Generuj graf", command=self.generate_and_color_graph)
        generate_button.pack()

        # Miejsce na rysunek grafu
        self.figure = plt.Figure(figsize=(9, 6), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, self.window)
        self.canvas.get_tk_widget().pack()
        self.ax.set_axis_off()

    def validate_positive_integer(self, value):
        try:
            val = int(value)
            return val > 0
        except ValueError:
            return False

    def validate_density(self, value):
        try:
            val = float(value)
            return 0 <= val <= 1
        except ValueError:
            return False

    def generate_and_color_graph(self):

        if not self.validate_positive_integer(self.vertices_entry.get()):
            messagebox.showerror("Błąd", "Liczba wierzchołków musi być dodatnią liczbą całkowitą.")
            return

        if not self.validate_positive_integer(self.colors_entry.get()):
            messagebox.showerror("Błąd", "Liczba kolorów musi być dodatnią liczbą całkowitą.")
            return

        if not self.validate_density(self.density_entry.get()):
            messagebox.showerror("Błąd", "Gęstość krawędzi musi być liczbą zmiennoprzecinkową od 0 do 1.")
            return

        try:
            num_vertices = int(self.vertices_entry.get())
            num_colors = int(self.colors_entry.get())
            edge_density = float(self.density_entry.get())

            g = Graph(num_vertices)
            g.generate_random_edges(edge_density)
            color = [0] * num_vertices

            if not graph_coloring(g, num_colors, color, 0):
                messagebox.showinfo("Wynik", "Nie istnieje poprawne kolorowanie dla {} kolorów.".format(num_colors))
            else:
                self.draw_graph(g, color)
                messagebox.showinfo("Wynik", "Istnieje poprawne kolorowanie dla {} kolorów.".format(num_colors))
        except ValueError:
            messagebox.showerror("Błąd", "Proszę wprowadzić poprawne dane.")

    def draw_graph(self, graph, color):
        self.ax.clear()
        G = nx.Graph()
        G.add_nodes_from(range(graph.vertices))
        G.add_edges_from([(u, v) for u in range(graph.vertices) for v in graph.graph[u] if u < v])

        pos = nx.spring_layout(G)
        nx.draw(G, pos, ax=self.ax, with_labels=True, node_color=color, cmap=plt.cm.Set3, node_size=500)
        self.canvas.draw()


# Uruchomienie aplikacji
if __name__ == "__main__":
    root = tk.Tk()
    app = GraphInterface(root)
    root.mainloop()
