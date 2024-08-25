memo = [None] * 100
counter = 0


def fib(n):
    global counter
    counter += 1
    # if the index in the list isn't empty, return the value in that index
    if memo[n] is not None:
        return memo[n]
    if n == 0 or n == 1:
        return n

    memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]


n = 7
print("\nFib of", n, "=", fib(n))
print("\nCounter:", counter)

print("-------------------")
n = 20
print("\nFib of", n, "=", fib(n))
print("\nCounter:", counter)

print("-------------------")
n = 30
print("\nFib of", n, "=", fib(n))
print("\nCounter:", counter)

print("-------------------")
n = 35
print("\nFib of", n, "=", fib(n))
print("\nCounter:", counter)
