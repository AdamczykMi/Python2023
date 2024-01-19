# Dokumentacja Programu "Kolorowanie Grafu"

## 1. Wprowadzenie

Program "Kolorowanie Grafu" jest aplikacją interaktywną, która demonstruje koncepcję kolorowania grafu w informatyce teoretycznej. Kolorowanie grafu polega na przypisaniu kolorów wierzchołkom grafu w taki sposób, aby żadne dwa sąsiadujące wierzchołki nie miały tego samego koloru. Program wykorzystuje algorytm z powrotami (backtracking) do znalezienia poprawnego kolorowania, jeśli jest to możliwe.

### Teoria Algorytmu
Algorytm kolorowania grafu jest przykładem problemu decyzyjnego, który jest klasyfikowany jako NP-trudny. Wymaga on znajdowania kombinacji kolorów dla wierzchołków, przy czym kolory sąsiadujących wierzchołków nie mogą się powtarzać. Program wykorzystuje podejście rekurencyjne z powrotami, które systematycznie sprawdza wszystkie możliwe kombinacje kolorów, aż do znalezienia rozwiązania lub stwierdzenia jego braku.

## 2. Opis Interfejsu

Interfejs użytkownika jest prosty i intuicyjny, zapewniając łatwe w użyciu narzędzie do eksploracji problemu kolorowania grafu.

### Elementy Interfejsu
- **Pola tekstowe**: Użytkownik wprowadza liczbę wierzchołków, liczbę kolorów oraz gęstość krawędzi grafu.
- **Przycisk "Generuj graf"**: Po wprowadzeniu danych, użytkownik klika ten przycisk, aby wygenerować i pokolorować graf.
- **Wizualizacja grafu**: Po wygenerowaniu i pokolorowaniu, graf jest wizualizowany na dole okna.

## 3. Uwagi na Temat Implementacji

Program został zaimplementowany w języku Python, z wykorzystaniem bibliotek `tkinter` dla interfejsu użytkownika, `matplotlib` do wizualizacji grafu oraz `networkx` do zarządzania strukturą grafu.

Oto szczegółowy opis działania i funkcji każdej części klasy `Graph`:


### 3.1. Klasa Graph
#### 3.1.1. Konstruktor `__init__(self, vertices)`

```python
def __init__(self, vertices):
    self.vertices = vertices
    self.graph = [[] for _ in range(vertices)]
```

- `__init__(self, vertices)` to konstruktor klasy `Graph`. Przyjmuje argument `vertices`, który określa liczbę wierzchołków w grafie.
- `self.vertices = vertices`: Przypisuje liczbę wierzchołków `vertices` do atrybutu `self.vertices`, aby przechować tę informację w obiekcie grafu.
- `self.graph = [[] for _ in range(vertices)]`: Inicjuje strukturę grafu jako listę list. Każdy wierzchołek ma swoją listę sąsiadujących wierzchołków. Na początku, wszystkie listy są puste, ponieważ graf nie ma żadnych krawędzi. `self.graph` jest używane do przechowywania struktury grafu.

#### 3.1.2. Metoda `add_edge(self, u, v)`

```python
def add_edge(self, u, v):
    self.graph[u].append(v)
    self.graph[v].append(u)
```

- `add_edge(self, u, v)` to metoda, która służy do dodawania krawędzi między wierzchołkami `u` i `v` w grafie.
- `self.graph[u].append(v)`: Dodaje wierzchołek `v` do listy sąsiadujących wierzchołków wierzchołka `u`, co oznacza, że `u` i `v` są połączone krawędzią.
- `self.graph[v].append(u)`: Dodaje wierzchołek `u` do listy sąsiadujących wierzchołków wierzchołka `v`. Graf jest nieskierowany, więc dodaje się krawędź zarówno od `u` do `v`, jak i od `v` do `u`.

#### 3.1.3. Metoda `generate_random_edges(self, density)`

```python
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
```

- `generate_random_edges(self, density)` to metoda, która generuje losowe krawędzie w grafie na podstawie zadanej gęstości.
- `max_edges = (self.vertices * (self.vertices - 1)) // 2`: Oblicza maksymalną liczbę krawędzi w grafie pełnym o `self.vertices` wierzchołkach. Wykorzystywane do ograniczenia liczby krawędzi w zależności od zadanej gęstości.
- `num_edges = int(density * max_edges)`: Oblicza liczbę krawędzi, która zostanie wygenerowana na podstawie zadanej gęstości.
- `edges_added = 0`: Inicjalizuje licznik dodanych krawędzi.
- `while edges_added < num_edges`: Rozpoczyna pętlę, która będzie dodawać losowe krawędzie, dopóki nie zostanie osiągnięta zadana liczba krawędzi.
- `u = random.randint(0, self.vertices - 1)`: Losowo wybiera wierzchołek `u` z zakresu od 0 do `self.vertices - 1`.
- `v = random.randint(0, self.vertices - 1)`: Losowo wybiera wierzchołek `v` z zakresu od 0 do `self.vertices - 1`.
- `if u != v and v not in self.graph[u]`: Sprawdza, czy wybrane wierzchołki `u` i `v` nie są takie same i czy krawędź między nimi jeszcze nie istnieje w grafie. Jeśli te warunki są spełnione, dodaje krawędź między nimi za pomocą `self.add_edge(u, v)`.
- `edges_added += 1`: Zwiększa licznik dodanych krawędzi po udanym dodaniu krawędzi.


### 3.2. Funkcje kolorowania grafu

#### 3.2.1. Funkcja `is_safe(vertex, color, graph, c)`

```python
def is_safe(vertex, color, graph, c):
    for neighbor in graph[vertex]:
        if color[neighbor] == c:
            return False
    return True
```

- `is_safe(vertex, color, graph, c)` sprawdza, czy można bezpiecznie przypisać kolor `c` do wierzchołka `vertex` w grafie. Działa w następujący sposób:
  - `vertex` to wierzchołek, któremu chcemy przypisać kolor `c`.
  - `color` to tablica kolorów, gdzie `color[i]` reprezentuje przypisany kolor do wierzchołka `i`.
  - `graph` to struktura grafu, a `graph[vertex]` zawiera listę sąsiadujących wierzchołków z wierzchołkiem `vertex`.
  - `c` to kolor, który chcemy przypisać wierzchołkowi `vertex`.
- Funkcja iteruje przez listę sąsiadujących wierzchołków `neighbor` wierzchołka `vertex`.
- Dla każdego sąsiada sprawdza, czy sąsiad ma ten sam kolor `c` jak wierzchołek `vertex`.
- Jeśli znaleziono choć jednego sąsiada o tym samym kolorze, funkcja zwraca `False`, co oznacza, że przypisanie koloru `c` do wierzchołka `vertex` jest niebezpieczne (koliduje z kolorem sąsiada).
- Jeśli żaden sąsiad nie ma tego samego koloru, funkcja zwraca `True`, co oznacza, że przypisanie koloru `c` do wierzchołka `vertex` jest bezpieczne.

#### 3.2.2. Funkcja `graph_coloring(graph, m, color, v)`

```python
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
```

- `graph_coloring(graph, m, color, v)` to główna funkcja algorytmu kolorowania grafu przy użyciu rekurencyjnego podejścia z powrotami.
- `graph` To obiekt grafu, który ma zostać pokolorowany.
- `m` Maksymalna liczba dostepnych kolorów.
- `color` Lista, w której indeks odpowiada numerowi wierzchołka, a wartość w liście to kolor przypisany danemu wierzchołkowi. Początkowo wszystkie wartości w tej liście są ustawione na 0, co oznacza, że żaden wierzchołek jeszcze nie jest pokolorowany.
- `v` Bieżący wierzchołek, do którego algorytm próbuje przypisać kolor.
- Algorytm iteruje przez wszystkie możliwe kolory od 1 do m. Dla każdego koloru c sprawdza, czy może być bezpiecznie przypisany do bieżącego wierzchołka v.
- Jeśli `v` osiągnie wartość `graph.vertices`, oznacza to, że wszystkie wierzchołki zostały pokolorowane, więc algorytm zwraca `True` (poprawne kolorowanie zostało znalezione).
- W pętli `for c in range(1, m + 1)`, algorytm próbuje przypisać kolor `c` do wierzchołka `v`.
- Przed przypisaniem koloru sprawdzane jest, czy jest to bezpieczne przypisanie, używając funkcji `is_safe(v, color, graph.graph, c)`. Jeśli tak, kolor jest przypisywany do wierzchołka `(color[v] = c)`.
- Następnie algorytm wywołuje się rekurencyjnie dla następnego wierzchołka (v + 1).
- Jeśli rekurencyjne wywołanie zwróci `True`, to znaczy, że udało się znaleźć poprawne kolorowanie reszty grafu, więc algorytm zwraca `True`.
- Jeśli żaden z kolorów nie jest bezpieczny lub rekurencyjne wywołanie dla koloru c zwróci False, algorytm wykonuje krok wstecz (cofając przypisanie koloru, ustawiając color[v] = 0). Następnie algorytm kontynuuje iterację po kolejnych kolorach.
- Jeśli wszystkie kolory zostały wypróbowane dla wierzchołka `v` i nie udało się znaleźć poprawnego kolorowania, algorytm zwraca `False`.

### 3.3. Klasa `GraphInterface`

#### 3.3.1 Konstruktor `__init__(self, window)`
```python
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
```

Ten fragment kodu definiuje konstruktor `__init__` klasy `GraphInterface`, który jest odpowiedzialny za inicjalizację interfejsu użytkownika oraz przygotowanie miejsca do wyświetlenia grafu.

Oto opis poszczególnych elementów tego konstruktora:

- `def __init__(self, window)`: Konstruktor jest wywoływany podczas tworzenia instancji klasy `GraphInterface` i przyjmuje jeden argument `window`, który reprezentuje okno aplikacji, w którym interfejs będzie działał.

- `self.window = window`: Przypisanie okna głównego do atrybutu `self.window`, aby można było odwoływać się do niego w innych częściach klasy.

- `self.window.title("Kolorowanie Grafu")`: Ustawienie tytułu okna na "Kolorowanie Grafu".

- `tk.Label(window, text="Liczba wierzchołków:").pack()`: Tworzenie etykiety (label) z tekstem "Liczba wierzchołków" i umieszczenie jej w oknie głównym.

- `self.vertices_entry = tk.Entry(window)`: Tworzenie pola tekstowego (entry) i przypisanie go do atrybutu `self.vertices_entry`. To pole służy do wprowadzania liczby wierzchołków grafu.

- `self.vertices_entry.pack()`: Umieszczenie pola tekstowego w oknie głównym.

- Podobnie jak powyżej, są tworzone etykiety i pola tekstowe dla liczby kolorów i gęstości krawędzi.

- `generate_button = tk.Button(window, text="Generuj graf", command=self.generate_and_color_graph)`: Tworzenie przycisku "Generuj graf" i przypisanie mu funkcji `self.generate_and_color_graph` jako akcji do wykonania po kliknięciu.

- `generate_button.pack()`: Umieszczenie przycisku w oknie głównym.

- `self.figure = plt.Figure(figsize=(9, 6), dpi=100)`: Utworzenie figury (wykresu) za pomocą biblioteki `matplotlib`. Ta figura będzie używana do rysowania grafu.

- `self.ax = self.figure.add_subplot(111)`: Utworzenie subplotu na wykresie i przypisanie go do atrybutu `self.ax`. Subplot ten będzie wykorzystywany do rysowania grafu.

- `self.canvas = FigureCanvasTkAgg(self.figure, self.window)`: Tworzenie obiektu `FigureCanvasTkAgg`, który jest interfejsem pomiędzy figurą `self.figure` a biblioteką `tkinter`.

- `self.canvas.get_tk_widget().pack()`: Umieszczenie interfejsu do rysowania figury w oknie głównym.

- `self.ax.set_axis_off()`: Wyłączenie osi na subplotcie, co oznacza brak wyświetlanych osi na wykresie.

Ten konstruktor inicjuje więc interfejs użytkownika, tworzy pola tekstowe, przycisk generowania grafu i przygotowuje miejsce na wyświetlenie grafu.

### 3.3.2 Metody `validate_positive_integer(self, value)` i `validate_density(self, value)`
```python
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
```

- `validate_positive_integer(self, value)`: Ta funkcja przyjmuje dwa argumenty, `self` (co oznacza, że jest to metoda instancji klasy) i `value`, który jest wartością do walidacji. Funkcja próbuje przekształcić `value` w liczbę całkowitą przy użyciu funkcji `int(value)`. Jeśli to się powiedzie i wartość jest liczbą całkowitą większą od zera, funkcja zwraca `True`, co oznacza, że wartość jest poprawna. Jeśli przekształcenie lub warunek nie są spełnione, funkcja zwraca `False`, co oznacza, że wartość jest niepoprawna.

- `validate_density(self, value)`: Ta funkcja również przyjmuje dwa argumenty, `self` i `value`. Podobnie jak wcześniej, próbuje przekształcić `value` w liczbę zmiennoprzecinkową za pomocą `float(value)`. Jeśli to się powiedzie i wartość mieści się w zakresie od 0 do 1 (włącznie), funkcja zwraca `True`, co oznacza, że wartość jest poprawna jako gęstość krawędzi. Jeśli przekształcenie lub warunek nie są spełnione, funkcja zwraca `False`, co oznacza, że wartość jest niepoprawna jako gęstość krawędzi.

Te dwie funkcje są używane w interfejsie użytkownika (`GraphInterface`), aby zweryfikować poprawność danych wprowadzonych przez użytkownika przed próbą generowania i kolorowania grafu. Jeśli wprowadzone dane nie spełniają tych warunków, użytkownik zostanie poinformowany o błędzie.

### 3.3.3 Metoda `generate_and_color_graph(self)`
```python
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
```
### 3.3.4 Metoda `draw_graph(self, graph, color)`
Funkcja `generate_and_color_graph` jest kluczowym elementem interfejsu użytkownika (`GraphInterface`). Oto opis jej działania:

- **Walidacja Danych Wejściowych**: Na początku funkcja wykonuje trzy walidacje danych wprowadzonych przez użytkownika:

   - Sprawdza, czy liczba wierzchołków jest dodatnią liczbą całkowitą za pomocą funkcji `validate_positive_integer(self.vertices_entry.get())`. Jeśli to nie jest prawda, wyświetla błąd z komunikatem "Liczba wierzchołków musi być dodatnią liczbą całkowitą." i przerywa działanie funkcji.
   - Podobnie, sprawdza, czy liczba kolorów jest dodatnią liczbą całkowitą.
   - Sprawdza, czy gęstość krawędzi jest liczbą zmiennoprzecinkową od 0 do 1.

- **Tworzenie Grafu i Kolorowanie**:
   - Jeśli wszystkie dane są poprawne, funkcja próbuje przekształcić wprowadzone dane w odpowiednie typy (liczby całkowite i zmiennoprzecinkowe).
   - Tworzy instancję klasy `Graph` o liczbie wierzchołków `num_vertices`.
   - Wywołuje metodę `generate_random_edges` na obiekcie `g`, generując losowe krawędzie na podstawie wprowadzonej gęstości `edge_density`.
   - Inicjuje tablicę kolorów `color` o długości `num_vertices`.
   - Wywołuje funkcję `graph_coloring`, próbując znaleźć poprawne kolorowanie dla grafu `g` przy użyciu `num_colors` kolorów. Jeśli nie jest to możliwe, wyświetla komunikat, że nie istnieje poprawne kolorowanie.
   - Jeśli poprawne kolorowanie zostanie znalezione, wywołuje metodę `draw_graph` w celu wizualizacji wynikowego grafu z przypisanymi kolorami.

- **Komunikaty dla Użytkownika**:
   - Jeśli dane wejściowe są nieprawidłowe (np. niepoprawny format), użytkownik zostanie poinformowany o błędzie i działanie funkcji zostanie zatrzymane.
   - Po przetworzeniu danych i ewentualnym znalezieniu poprawnego kolorowania, funkcja wyświetla komunikaty za pomocą `messagebox.showinfo`.

Ogólnie rzecz biorąc, funkcja `generate_and_color_graph` zarządza całym procesem generowania grafu, próby jego kolorowania i prezentacji wyników użytkownikowi w interfejsie. Jeśli wystąpią błędy, są one obsługiwane poprzez wyświetlanie odpowiednich komunikatów.

```python
    def draw_graph(self, graph, color):
        self.ax.clear()
        G = nx.Graph()
        G.add_nodes_from(range(graph.vertices))
        G.add_edges_from([(u, v) for u in range(graph.vertices) for v in graph.graph[u] if u < v])

        pos = nx.spring_layout(G)
        nx.draw(G, pos, ax=self.ax, with_labels=True, node_color=color, cmap=plt.cm.Set3, node_size=500)
        self.canvas.draw()
```
Ten fragment kodu jest odpowiedzialny za wizualizację grafu z przypisanymi kolorami w interfejsie użytkownika. Oto opis jego działania:

- `self.ax.clear()`: Ta linia kodu czyści poprzednią wizualizację, jeśli istniała, aby można było narysować nowy graf.

- Tworzenie grafu wizualizacji:
   - `G = nx.Graph()`: Tworzy obiekt grafu za pomocą biblioteki NetworkX.
   - `G.add_nodes_from(range(graph.vertices))`: Dodaje wierzchołki do grafu wizualizacji, gdzie `graph.vertices` to liczba wierzchołków w oryginalnym grafie.
   - `G.add_edges_from([(u, v) for u in range(graph.vertices) for v in graph.graph[u] if u < v])`: Dodaje krawędzie między wierzchołkami grafu wizualizacji. To odzwierciedla strukturę grafu oryginalnego, ignorując krawędzie, które zostały dodane dwukrotnie (graf jest nieskierowany).

- `pos = nx.spring_layout(G)`: Określa układ wizualizacji grafu za pomocą algorytmu rozmieszczania wiosny (spring layout) z biblioteki NetworkX. Ten układ stara się rozmieścić wierzchołki w grafie tak, aby były one równomiernie rozłożone i nie nachodziły na siebie.

- `nx.draw(G, pos, ax=self.ax, with_labels=True, node_color=color, cmap=plt.cm.Set3, node_size=500)`: Ta linia kodu rysuje graf wizualizacji na podstawie utworzonej struktury `G`. Oto, co robi każdy z jej argumentów:
   - `G`: Graf wizualizacji, który ma być narysowany.
   - `pos`: Układ wierzchołków w grafie.
   - `ax=self.ax`: Określa, na jakiej osi matplotlib ma narysować graf. W tym przypadku używamy wcześniej zdefiniowanej osi `self.ax`.
   - `with_labels=True`: Rysuje etykiety wierzchołków z ich numerami.
   - `node_color=color`: Określa kolor wierzchołków zgodnie z przypisanymi kolorami z tablicy `color`.
   - `cmap=plt.cm.Set3`: Wybiera mapę kolorów do używania w przypadku, gdy jest więcej kolorów niż dostępnych domyślnie.
   - `node_size=500`: Określa rozmiar wierzchołków w wizualizacji.

- `self.canvas.draw()`: Aktualizuje widok canvasa (elementu GUI, na którym jest rysowana wizualizacja), aby pokazać nowy graf z przypisanymi kolorami.

Ogólnie rzecz biorąc, ten fragment kodu służy do rysowania grafu wizualizacji z przypisanymi kolorami w oknie interfejsu użytkownika, aby użytkownik mógł zobaczyć wynik kolorowania grafu.

Implementacja programu "Kolorowanie Grafu" jest oparta na obiektowości, co ułatwia zarządzanie kodem i interakcję z użytkownikiem. Algorytm kolorowania grafu jest zaimplementowany w sposób rekurencyjny, umożliwiając systematyczne przeszukiwanie możliwych rozwiązań. Interfejs użytkownika jest prosty i intuicyjny, co ułatwia korzystanie z programu.

## 4. Podsumowanie i Wyniki Testów


### 4.1 `test_add_edge`:
   - Kod testu:
     ```python
     def test_add_edge(self):
         graph = Graph(4)
         graph.add_edge(0, 1)
         self.assertIn(1, graph.graph[0])
         self.assertIn(0, graph.graph[1])
     ```
   - Ten test tworzy obiekt grafu o 4 wierzchołkach, a następnie dodaje krawędź między wierzchołkami 0 i 1 za pomocą `graph.add_edge(0, 1)`. Następnie sprawdza, czy w grafie istnieją odpowiednie krawędzie, tj. `0` w liście sąsiedztwa wierzchołka `1` i `1` w liście sąsiedztwa wierzchołka `0`. To sprawdzenie jest wykonane za pomocą `self.assertIn`.

### 4.2 `test_generate_random_edges`:
   - Kod testu:
     ```python
     def test_generate_random_edges(self):
         graph = Graph(4)
         graph.generate_random_edges(0.5)
         total_edges = sum(len(v) for v in graph.graph) // 2
         self.assertGreaterEqual(total_edges, 1)
     ```
   - Ten test tworzy obiekt grafu o 4 wierzchołkach, a następnie generuje losowe krawędzie w grafie na podstawie gęstości 0.5 za pomocą `graph.generate_random_edges(0.5)`. Następnie oblicza całkowitą liczbę krawędzi w grafie i sprawdza, czy jest większa lub równa 1. To sprawdzenie jest wykonane za pomocą `self.assertGreaterEqual`.

### 4.3 `test_is_safe`:
   - Kod testu:
     ```python
     def test_is_safe(self):
         graph = Graph(3)
         graph.add_edge(0, 1)
         color = [1, 2, 0]
         self.assertTrue(is_safe(2, color, graph.graph, 1))
     ```
   - Ten test tworzy obiekt grafu o 3 wierzchołkach, a następnie dodaje krawędź między wierzchołkami 0 i 1 za pomocą `graph.add_edge(0, 1)`. Tworzy listę kolorów `[1, 2, 0]`, gdzie wierzchołek 2 ma przypisany kolor 0. Następnie sprawdza, czy funkcja `is_safe(2, color, graph.graph, 1)` zwraca `True`, co oznacza, że jest bezpieczne przypisanie koloru 1 do wierzchołka 2, ponieważ nie sąsiaduje on z żadnym innym wierzchołkiem o tym samym kolorze.

### 4.4 `test_graph_coloring`:
   - Kod testu:
     ```python
     def test_graph_coloring(self):
         graph = Graph(3)
         graph.add_edge(0, 1)
         graph.add_edge(1, 2)
         color = [0] * 3
         self.assertTrue(graph_coloring(graph, 3, color, 0))
         self.assertNotEqual(color, [0] * 3)
     ```
   - Ten test tworzy obiekt grafu o 3 wierzchołkach i dodaje dwie krawędzie: 0 -> 1 i 1 -> 2. Następnie tworzy listę kolorów `[0, 0, 0]`, co oznacza, że początkowo wszystkie wierzchołki są bez koloru. Sprawdza, czy funkcja `graph_coloring` jest w stanie przypisać kolory do wierzchołków w taki sposób, że żadne dwa sąsiednie wierzchołki nie mają tego samego koloru, co jest potwierdzone przez `self.assertTrue`. Dodatkowo sprawdza, czy lista kolorów nie jest równa początkowej liście `[0, 0, 0]`, co oznacza, że kolory zostały przypisane poprawnie, co jest potwierdzone przez `self.assertNotEqual`.

Wszystkie testy zakończyły się bez błędów, potwierdzając poprawność działania odpowiednich funkcji i metod w projekcie.
## 5. Literatura i Źródła

- https://matplotlib.org/stable/contents.html
- https://docs.python.org/3/library/tkinter.html
- https://www.geeksforgeeks.org/m-coloring-problem/
- https://www.geeksforgeeks.org/graph-coloring-applications/
---
