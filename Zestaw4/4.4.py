def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_sequence = [0, 1]

        for i in range(2, n + 1):
            fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

        return fib_sequence[n]


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(15))
print(fibonacci_iterative(0))
print(fibonacci_iterative(1))
print(fibonacci_iterative(45))