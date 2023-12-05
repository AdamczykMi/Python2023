class AlternatingIterator:
    def __init__(self):
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.value
        self.value = 1 - self.value
        return result

iterator_a = AlternatingIterator()
for _ in range(10):
    print(next(iterator_a))
