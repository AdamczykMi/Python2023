def reverse(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


def reverse_rek(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        reverse_rek(L, left + 1, right - 1)

lista = [1, 7, 3, 8, 5]
#reverse(lista, 1, 3)
reverse_rek(lista, 1, 3)
print(lista)