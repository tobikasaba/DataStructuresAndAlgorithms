# This piece of code is know as O(n) where n is the number of operations.
# Hence, in this case, there were 10 Operations
def print_items(n):
    for i in range(n):
        print(i)

    # drop constant
    for j in range(n):
        print(j)


# (print_items(10))

# O(n^2)
# Here we have n*n (100 items) printed out hence n^2
# The function ran both O(n^2) and O(n)
# altogether the function ran O(n^2 + n)
# In this, n^2 is the dominant, larger operation and just n is the non-dominant
def print_items_two(n):
    # O(n^2)
    for i in range(n):
        for j in range(n):
            print(i, j)
    # O(n)
    for k in range(n):
        print(k)

print(print_items_two(10))

# O(1)
# The number of operations remanins the same regardless of the value of n
# this is also known as constant time meaning as n increases the number of operations will remain constant
def add_itmes(n):
    return n+n