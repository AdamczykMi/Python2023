result = ""

length = input("podaj długość linijki: ")
length = int(length)

for i in "|...." * length:
    result += i
result += '|\n0'

for i in range(1, length + 1):
    result = result + (" " * (5 - len(str(i)))) + str(i)

print(result)

