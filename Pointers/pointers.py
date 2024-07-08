# creates an interger 11 in memory and point the variable num_1 at that integer
num_1 = 11
# assigns num 2 also to that integer in memory
num_2 = num_1

print("Before num_2 values is updated:")
print("num_1 = ", num_1)
print("num_2 = ", num_2)

# this prints the address where num 1 and num 2 are stored
print("\nnum1 points to:", id(num_1))
print("num2 points to:", id(num_2))

# num_1  and num_ 2 have different values, then they have different values in memory
num_2 = 22
print("\nAfter num_2 values is updated:")
print("num_1 = ", num_1)
print("num_2 = ", num_2)

# this prints the address where num 1 and num 2 are stored
print("\nnum1 points to:", id(num_1))
print("num2 points to:", id(num_2))

# point to the same address in memory
dict_1 = {"value": 11}
dict_2 = dict_1

print("\nBefore num_2 values is updated:")
print(("dict_1 = ", dict_1))
print(("dict_2 = ", dict_2))

print("\nnum1 points to:", id(dict_1))
print("num2 points to:", id(dict_2))

# still points to the same address in memory because the value in the dictionary was changed not the dictionary itself
# Dictionaries are mutable, hence the value in the dictionary has changed
dict_2["value"] = 22
print(("dict_1 = ", dict_1))
print(("dict_2 = ", dict_2))

print("\nnum1 points to:", id(dict_1))
print("num2 points to:", id(dict_2))
