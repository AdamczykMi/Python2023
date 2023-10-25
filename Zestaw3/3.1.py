# poprawiony kod:
x = 2
y = 3
if x > y:
    result = x
else:
    result = y

for i in "axby":
    if ord(i) < 100:
        print(i)

for i in "axby":
    print(ord(i) if ord(i) < 100 else i)
"""
1 usunięcie średników przy inicjalizacji zmiennych
2 usunięcie nawiasów w warunku 
3 dodanie wcięc w kodach bloków pętli for
4 dodanie ":" po "axby"
"""