result = ""

a = input("Podaj dlugosc boku a: ")
a = int(a)

b = input("Podaj dlugosc boku b: ")
b = int(b)

for i in range(a):
    result += "+---" * b + "+\n"
    result += "|   " * b + "|\n"

result += "+---" * b + "+\n"

print(result)
