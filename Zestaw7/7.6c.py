class DayOfWeekIterator:
    def __init__(self):
        self.day = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.day
        self.day = (self.day + 1) % 7  # Cykliczne inkrementowanie dni tygodnia
        return result

# Przykład użycia:
iterator_c = DayOfWeekIterator()
for _ in range(14):
    print(next(iterator_c))
