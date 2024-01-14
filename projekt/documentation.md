## Dokumentacja projektu Kolorowanie Grafu

### 1. Wprowadzenie
Projekt Kolorowanie Grafu skupia się na wizualizacji i kolorowaniu losowych grafów generowanych przy użyciu biblioteki NetworkX. Głównym algorytmem używanym w tym projekcie jest algorytm backtrackingu, służący do kolorowania wierzchołków grafu.

### 2. Opis Interfejsu
Projekt Kolorowanie Grafu składa się z prostego interfejsu graficznego (GUI) utworzonego przy użyciu Tkinter. Kluczowe elementy interfejsu obejmują:

- **Pole Wprowadzania Liczby Wierzchołków:** Pole tekstowe, w którym użytkownicy wprowadzają liczbę wierzchołków, które chcą mieć w wygenerowanym grafie.
- **Przycisk Generowania Grafu:** Przycisk, który uruchamia generowanie losowego grafu na podstawie wprowadzonego przez użytkownika parametru.
- **Obszar Wizualizacji Grafu:** Plótno Matplotlib osadzone w GUI do wyświetlania wygenerowanego grafu z pokazanymi kolorami wierzchołków.

### 3. Szczegóły Implementacji

Projekt Kolorowanie Grafu został zaimplementowany w języku Python przy użyciu bibliotek NetworkX, Matplotlib i Tkinter. W tej sekcji omówione są kluczowe aspekty implementacyjne, z uwzględnieniem funkcji i metod klasy `Graph` oraz klasy `GUIApp`.

#### 3.1 Klasa `Graph`

##### 3.1.1 Metoda `__init__(self)`
Metoda ta jest konstruktorem klasy `Graph`. Inicjalizuje pustą strukturę grafu i listę kolorów.

```python
def __init__(self):
    self.graph = nx.Graph()
    self.colors = []
```

##### 3.1.2 Metoda `generate_random_graph(self, num_vertices, probability)`
Metoda `generate_random_graph` klasy `Graph` korzysta z funkcji `nx.fast_gnp_random_graph` z biblioteki NetworkX, która generuje losowy graf o zadanym rozmiarze i prawdopodobieństwie wystąpienia krawędzi między wierzchołkami. 

1. **Inicjalizacja pustego grafu**: Metoda rozpoczyna od utworzenia nowego obiektu grafu, który na początku jest pusty.

    ```python
    self.graph = nx.fast_gnp_random_graph(num_vertices, probability)
    ```

    Tutaj `num_vertices` to liczba wierzchołków w grafie, a `probability` to prawdopodobieństwo wystąpienia krawędzi między dowolną parą wierzchołków.

2. **Inicjalizacja listy kolorów**: Tworzy listę kolorów o długości równej liczbie wierzchołków w grafie, zainicjowaną wartościami -1. Kolor -1 oznacza, że wierzchołek nie został jeszcze pokolorowany.

    ```python
    self.colors = [-1] * len(self.graph.nodes)
    ```

3. **Przypisanie koloru do pierwszego wierzchołka**: Dla uproszczenia algorytmu kolorowania grafu, pierwszy wierzchołek (o indeksie 0) jest ręcznie pokolorowany na początku.

    ```python
    self.colors[0] = 0
    ```

Podsumowując, metoda `generate_random_graph` generuje losowy graf o zadanej liczbie wierzchołków i prawdopodobieństwie wystąpienia krawędzi między nimi, a następnie inicjalizuje listę kolorów i ręcznie pokolorowuje pierwszy wierzchołek.

##### 3.1.3 Metoda `is_safe(self, vertex, c)`
Metoda `is_safe` klasy `Graph` jest funkcją pomocniczą, która sprawdza, czy można bezpiecznie przypisać kolor `c` do wierzchołka `vertex` w grafie. 
Algorytm sprawdza, czy żaden z sąsiadów danego wierzchołka nie ma już przypisanego koloru. 
Jeśli żaden z sąsiadów nie ma tego samego koloru, to oznacza, że przypisanie koloru `c` wierzchołkowi `vertex` jest bezpieczne.



1. **Parametry wejściowe**: Metoda przyjmuje dwa parametry:
   - `vertex`: Numer wierzchołka, dla którego sprawdzane jest, czy można przypisać kolor.
   - `c`: Kolor, którego bezpieczeństwo przypisania jest sprawdzane.

    ```python
    def is_safe(self, vertex, c):
    ```

2. **Pętla po sąsiadach**: Metoda iteruje przez sąsiadów wierzchołka `vertex` przy użyciu `self.graph.neighbors(vertex)`. Dla każdego sąsiada sprawdza, czy ma już przypisany kolor `c`.

    ```python
    for neighbor in self.graph.neighbors(vertex):
        if self.colors[neighbor] == c:
            return False
    ```

    Jeśli znajdzie sąsiada o kolorze `c`, to zwraca `False`, oznaczając, że przypisanie koloru `c` wierzchołkowi `vertex` nie jest bezpieczne.

3. **Zwracanie wyniku**: Jeśli żaden sąsiad nie ma koloru `c`, to zwraca `True`, co oznacza, że przypisanie koloru `c` wierzchołkowi `vertex` jest bezpieczne.

    ```python
    return True
    ```

Podsumowując, metoda `is_safe` sprawdza, czy przypisanie danego koloru do danego wierzchołka jest bezpieczne, analizując kolory jego sąsiadów i zwracając odpowiednią wartość logiczną.

##### 3.1.4 Metoda `color_util(self, vertex)`
Metoda `color_util` klasy `Graph` jest funkcją pomocniczą do algorytmu kolorowania wierzchołków za pomocą algorytmu do tyłu (backtracking). Algorytm ten przypisuje kolory wierzchołkom w grafie w taki sposób, aby żadne dwa sąsiadujące wierzchołki nie miały tego samego koloru. Poniżej znajduje się dokładny opis działania tej metody:

1. **Parametr wejściowy**: Metoda przyjmuje jeden parametr `vertex`, który reprezentuje numer wierzchołka, dla którego aktualnie przypisywany jest kolor.

    ```python
    def color_util(self, vertex):
    ```

2. **Pętla po kolorach**: Metoda iteruje przez wszystkie dostępne kolory (oznaczone przez zmienną `c`). Dla każdego koloru sprawdza, czy można bezpiecznie przypisać ten kolor do wierzchołka `vertex` za pomocą wywołania metody `self.is_safe(vertex, c)`.

    ```python
    for c in range(len(self.graph.nodes)):
        if self.is_safe(vertex, c):
    ```

3. **Przypisanie koloru**: Jeśli znaleziono kolor, który może być bezpiecznie przypisany, ustawia ten kolor jako kolor wierzchołka `vertex` poprzez `self.colors[vertex] = c`.

    ```python
    self.colors[vertex] = c
    ```

4. **Rekurencyjne wywołanie**: Następnie sprawdza, czy istnieje kolejny wierzchołek (`vertex + 1 < len(self.graph.nodes)`). Jeśli tak, rekurencyjnie wywołuje samą siebie dla następnego wierzchołka (`self.color_util(vertex + 1)`).

    ```python
    if vertex + 1 < len(self.graph.nodes):
        if self.color_util(vertex + 1):
            return True
    ```

5. **Zakończenie lub cofnięcie kolorowania**: Jeśli udało się przypisać kolory wszystkim kolejnym wierzchołkom, zwraca `True`. W przeciwnym razie cofa przypisanie koloru dla bieżącego wierzchołka (`self.colors[vertex] = -1`) i kontynuuje iterację po kolejnych kolorach.

    ```python
    else:
        return True
    self.colors[vertex] = -1
    ```


##### 3.1.5 Metoda `color_graph(self)`
Metoda `color_graph` klasy `Graph` używa algorytmu (backtrackingu) do kolorowania wierzchołków grafu. Poniżej znajduje się dokładny opis działania tej metody:

1. **Wywołanie algorytmu do tyłu**: Metoda po prostu wywołuje funkcję pomocniczą `self.color_util(1)`, która jest algorytmem do tyłu odpowiedzialnym za kolorowanie wierzchołków.

    ```python
    def color_graph(self):
        self.color_util(1)
    ```

2. **Parametr wejściowy algorytmu do tyłu**: Algorytm do tyłu, czyli funkcja `self.color_util`, przyjmuje jeden parametr `vertex`, który reprezentuje numer wierzchołka, dla którego aktualnie przypisywany jest kolor.

    ```python
    def color_util(self, vertex):
    ```

3. **Rozpoczęcie procesu kolorowania**: Algorytm do tyłu rozpoczyna proces kolorowania od wierzchołka o numerze 1 (`self.color_util(1)`).

4. **Rekurencyjne kolorowanie**: Algorytm rekurencyjnie przypisuje kolory dla kolejnych wierzchołków, korzystając z funkcji pomocniczej `self.is_safe` do sprawdzania, czy dany kolor może być bezpiecznie przypisany do wierzchołka. Jeśli uda się przypisać kolory wszystkim wierzchołkom, to algorytm zakończy się, a przypisane kolory zostaną zapisane w atrybucie `self.colors`.

W rezultacie, metoda `color_graph` inicjuje proces kolorowania wierzchołków w grafie za pomocą algorytmu do tyłu, który stara się znaleźć poprawne przypisanie kolorów, aby żadne dwa sąsiadujące wierzchołki nie miały tego samego koloru.

##### 3.1.6 Metoda `draw_colored_graph(self, canvas)`
Metoda `draw_colored_graph` klasy `Graph` służy do rysowania wizualizacji kolorowanego grafu na dostarczonym plótnie Matplotlib. Poniżej znajduje się dokładny opis działania tej metody:

1. **Pobranie układu wierzchołków**: Używając funkcji `nx.spring_layout`, metoda uzyskuje układ wierzchołków grafu w przestrzeni, który jest używany do odpowiedniego rozmieszczenia wizualizacji.

    ```python
    pos = nx.spring_layout(self.graph)
    ```

2. **Rysowanie grafu**: Metoda używa funkcji `nx.draw` do narysowania grafu na dostarczonym plótnie (`canvas`). Parametry funkcji `nx.draw` obejmują:
    - `self.graph`: graf do narysowania,
    - `pos`: układ wierzchołków,
    - `with_labels=True`: dodanie etykiet wierzchołków,
    - `node_color=self.colors`: przypisanie kolorów wierzchołkom zgodnie z atrybutem `self.colors`,
    - `cmap=plt.cm.rainbow`: mapa kolorów używana do oznaczania różnych kolorów wierzchołków,
    - `font_color='white'`: kolor etykiet wierzchołków.

    ```python
    nx.draw(self.graph, pos, with_labels=True, node_color=self.colors, cmap=plt.cm.rainbow, font_color='white')
    ```

3. **Odświeżenie widoku canvas**: Ostatnią operacją jest wywołanie `canvas.draw()`, co odświeża widok Matplotlib na dostarczonym plótnie.

    ```python
    canvas.draw()
    ```

W rezultacie, metoda `draw_colored_graph` generuje wizualizację grafu, gdzie wierzchołki są kolorowane zgodnie z przypisanymi kolorami, a sam graf jest rozmieszczony w przestrzeni według określonego układu.

#### 3.2 Klasa `GUIApp`

Klasa `GUIApp` jest interfejsem graficznym użytkownika (GUI) do obsługi generowania i wizualizacji kolorowanych grafów. Poniżej znajduje się dokładny opis istotnych metod klasy:

##### 3.2.1 Metoda `__init__(self, root)`
Konstruktor klasy inicjalizuje obiekt `GUIApp` i tworzy główne okno interfejsu użytkownika. Parametr `root` to obiekt Tkinter, który pełni rolę głównego okna.

- **Tworzenie głównego okna:**
  ```python
  self.root = root
  self.root.title("Graph Colorization")
  ```

- **Inicjalizacja obiektu `Graph`:**
  ```python
  self.graph = Graph()
  ```

- **Tworzenie etykiety i pola wprowadzania liczby wierzchołków:**
  ```python
  self.total_vertices_label = tk.Label(root, text="Liczba wierzchołków w grafie:")
  self.total_vertices_label.pack()
  self.total_vertices_entry = tk.Entry(root)
  self.total_vertices_entry.pack()
  ```

- **Tworzenie przycisku "Generuj graf" i przypisanie metody `generate_graph` jako funkcji wywoływanej po naciśnięciu:**
  ```python
  self.generate_button = tk.Button(root, text="Generuj graf", command=self.generate_graph)
  self.generate_button.pack()
  ```

- **Inicjalizacja obiektu `FigureCanvasTkAgg` do rysowania wizualizacji grafu:**
  ```python
  self.figure, self.ax = plt.subplots(figsize=(10, 8))
  self.canvas = FigureCanvasTkAgg(self.figure, master=root)
  self.canvas.get_tk_widget().pack()
  self.ax.set_axis_off()
  ```

- **Dodanie warunków dla pola Entry, aby akceptować tylko cyfry:**
  ```python
  self.total_vertices_entry.config(validate="key", validatecommand=(root.register(validate_entry), "%P"))
  ```

##### 3.2.2 Metoda `generate_graph(self)`

Metoda `generate_graph` jest wywoływana po naciśnięciu przycisku "Generuj graf". Odpowiada za generowanie losowego grafu, kolorowanie go za pomocą algorytmu `color_graph` z klasy `Graph` oraz rysowanie kolorowanego grafu na interfejsie użytkownika.

- **Pobranie liczby wierzchołków z pola wprowadzania:**
  ```python
  total_vertices_input = self.total_vertices_entry.get()
  ```

- **Sprawdzenie, czy użytkownik wprowadził liczbę wierzchołków:**
  ```python
  if not total_vertices_input:
      tk.messagebox.showerror("Błąd", "Proszę wpisać liczbę wierzchołków przed generowaniem grafu.")
      return
  ```

- **Konwersja wprowadzonej liczby wierzchołków na liczbę całkowitą:**
  ```python
  total_vertices = int(total_vertices_input)
  ```

- **Generowanie losowego grafu, kolorowanie go i rysowanie na interfejsie użytkownika:**
  ```python
  self.graph.generate_random_graph(total_vertices, probability=0.4)
  self.graph.color_graph()
  self.ax.clear()
  self.graph.draw_colored_graph(self.canvas)
  ```

W rezultacie, metoda `generate_graph` obsługuje cały proces generowania, kolorowania i rysowania kolorowanego grafu na interfejsie użytkownika po wprowadzeniu odpowiednich parametrów.

#### 4. Podsumowanie i Wyniki Testów

##### Opis testów jednostkowych

##### 1. `test_generate_graph_with_valid_input`

- **Cel testu:** Sprawdzenie, czy metoda `generate_graph` działa poprawnie dla poprawnych danych wejściowych.
  
- **Opis testu:** Wstawienie poprawnej liczby wierzchołków (5) do pola wprowadzania, a następnie wywołanie metody `generate_graph`. Sprawdzenie, czy brak jest błędów w standardowym strumieniu wyjścia (stdout).

- **Oczekiwany wynik:** Brak błędów na standardowym strumieniu wyjścia.

##### 2. `test_generate_graph_with_invalid_input`

- **Cel testu:** Sprawdzenie, czy metoda `generate_graph` obsługuje poprawnie błędne dane wejściowe.

- **Opis testu:** Wywołanie metody `generate_graph` bez podania liczby wierzchołków. Sprawdzenie, czy został wywołany komunikat błędu za pomocą `showerror` z `tk.messagebox`.

- **Oczekiwany wynik:** Wywołanie komunikatu błędu "Proszę wpisać liczbę wierzchołków przed generowaniem grafu." i brak błędów na standardowym strumieniu wyjścia.

##### 3. `test_generate_random_graph`

- **Cel testu:** Sprawdzenie, czy metoda `generate_random_graph` klasy `Graph` generuje poprawny losowy graf.

- **Opis testu:** Wywołanie metody `generate_random_graph` z liczbą wierzchołków równą 5 i prawdopodobieństwem 0.4. Sprawdzenie, czy graf został poprawnie utworzony, czy liczba wierzchołków oraz kolory zostały prawidłowo zainicjalizowane.

- **Oczekiwany wynik:** Poprawne utworzenie grafu o 5 wierzchołkach, zainicjalizowanie odpowiedniej liczby kolorów, a pierwszy wierzchołek pokolorowany na 0.

##### 4. `test_color_graph`

- **Cel testu:** Sprawdzenie, czy metoda `color_graph` klasy `Graph` poprawnie koloruje graf.

- **Opis testu:** Wygenerowanie losowego grafu i wywołanie metody `color_graph`. Sprawdzenie, czy wszystkie wierzchołki są pokolorowane, czy kolorowanie jest poprawne (brak takich samych kolorów dla sąsiadujących wierzchołków).

- **Oczekiwany wynik:** Wszystkie wierzchołki są pokolorowane, brak takich samych kolorów dla sąsiadujących wierzchołków.

##### 5. `test_generate_graph_calls_draw_colored_graph`

- **Cel testu:** Sprawdzenie, czy metoda `generate_graph` klasy `GUIApp` wywołuje poprawnie metodę rysującą kolorowany graf.

- **Opis testu:** Wstawienie liczby wierzchołków i wywołanie metody `generate_graph`. Sprawdzenie, czy metoda `draw_colored_graph` z klasy `Graph` została poprawnie wywołana.

- **Oczekiwany wynik:** Metoda `draw_colored_graph` została wywołana dokładnie raz.

---

Wszystkie testy zakończyły się bez błędów, potwierdzając poprawność działania odpowiednich funkcji i metod w projekcie.
#### 5. Referencje
Do stworzenia tego projektu wykorzystano następujące biblioteki i zasoby:

-  [https://matplotlib.org/stable/contents.html](https://matplotlib.org/stable/contents.html)
-  [https://docs.python.org/3/library/tkinter.html](https://docs.python.org/3/library/tkinter.html)
-  https://www.geeksforgeeks.org/m-coloring-problem/