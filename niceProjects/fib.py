def fib(n, n2):
    if n2 > 10000:
        return
    print(n2, end=" ")
    fib(n2, n + n2)

fib(1, 1)
