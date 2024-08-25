counter = 0


def fib(n):
    fib_list = [0, 1]
    global counter

    for index in range(2, n + 1):
        counter += 1
        next_fib = fib_list[index - 1] + fib_list[index - 2]
        fib_list.append(next_fib)
    return fib_list[n]


n = 7
print("\nFib of", n, "=", fib(n))
print("\nCounter:", counter)

print("-------------------")
n = 35
print("\nFib of", n, "=", fib(n))
print("\nCounter:", counter)
