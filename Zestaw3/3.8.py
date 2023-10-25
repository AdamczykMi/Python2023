sequence1 = [1, 2, 3, 4, 5]
sequence2 = [3, 3, 4, 5, 6, 7]

common = list(set(sequence1) & set(sequence2))

all = list(set(sequence1) | set(sequence2))

print("Common Elements:", common)
print("All Elements:", all)

