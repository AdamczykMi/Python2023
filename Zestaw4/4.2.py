def make_ruler(n):
    result = ""
    for i in "|...." * n:
        result += i
    result += '|\n0'

    for i in range(1, n + 1):
        result = result + (" " * (5 - len(str(i)))) + str(i)

    return result

def make_grid(rows, cols):
    result = ""

    for i in range(rows):
        result += "+---" * cols + "+\n"
        result += "|   " * cols + "|\n"

    result += "+---" * cols + "+\n"

    return result

print(make_ruler(10))
print(make_grid(3,4))