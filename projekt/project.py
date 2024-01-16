import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Graph:
    def __init__(self):
        self.graph = nx.Graph()
        self.colors = []

    def generate_random_graph(self, num_vertices, probability):
        self.graph = nx.fast_gnp_random_graph(num_vertices, probability)
        self.colors = [-1] * len(self.graph.nodes)
        self.colors[0] = 0

    def color_graph(self):
        def is_safe(vertex, c):
            for neighbor in self.graph.neighbors(vertex):
                if self.colors[neighbor] == c:
                    return False
            return True

        def color_util(vertex):
            for c in range(len(self.graph.nodes)):
                if is_safe(vertex, c):
                    self.colors[vertex] = c
                    if vertex + 1 < len(self.graph.nodes):
                        if color_util(vertex + 1):
                            return True
                    else:
                        return True
                    self.colors[vertex] = -1

        color_util(1)

    def draw_colored_graph(self, canvas):
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_color=self.colors, cmap=plt.cm.rainbow, font_color='white')
        canvas.draw()


def validate_entry(value):
    return value.isdigit() or value == ""


class GUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Colorization")

        self.graph = Graph()

        self.total_vertices_label = tk.Label(root, text="Liczba wierzchołków w grafie:")
        self.total_vertices_label.pack()
        self.total_vertices_entry = tk.Entry(root)
        self.total_vertices_entry.pack()

        self.generate_button = tk.Button(root, text="Generuj graf", command=self.generate_graph)
        self.generate_button.pack()


        self.figure, self.ax = plt.subplots(figsize=(10, 8))
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().pack()
        self.ax.set_axis_off()


        self.total_vertices_entry.config(validate="key", validatecommand=(root.register(validate_entry), "%P"))

        root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.root.quit()
        self.root.destroy()

    def generate_graph(self):
        total_vertices_input = self.total_vertices_entry.get()

        if not total_vertices_input:
            tk.messagebox.showerror("Błąd", "Proszę wpisać liczbę wierzchołków przed generowaniem grafu.")
            return

        total_vertices = int(total_vertices_input)
        self.graph.generate_random_graph(total_vertices, probability=0.4)
        self.graph.color_graph()

        self.ax.clear()
        self.graph.draw_colored_graph(self.canvas)


if __name__ == "__main__":
    main_root = tk.Tk()
    app = GUIApp(main_root)
    main_root.mainloop()


