counter = 0


def fib(n):
    # this allows the function to see the variable outside the function
    global counter
    counter += 1
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


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
