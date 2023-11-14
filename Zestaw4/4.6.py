def sum_seq(sequence):
    result = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            result += sum_seq(item)
        else:
            result += item
    return result

my_sequence = [1, 2, [3, 4, [5, 6]], (7, 8)]
print(sum_seq(my_sequence))