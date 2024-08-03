def factorial(num):
    ans = 0
    if num == 1:
        return 1
    return num * factorial(num - 1)


print(factorial(4))
