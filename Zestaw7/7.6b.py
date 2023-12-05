import random

class RandomIterator:
    def __iter__(self):
        return self

    def __next__(self):
        directions = ["N", "E", "S", "W"]
        return random.choice(directions)

# Przykład użycia:
iterator_b = RandomIterator()
for _ in range(10):
    print(next(iterator_b))

