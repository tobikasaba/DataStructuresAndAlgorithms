def has_unique_chars(string):
    unique_char = set()
    for char in string:
        if char in unique_char:
            return False
        unique_char.add(char)
    return True


print(has_unique_chars('abcdefg'))  # should return True
print(has_unique_chars('hello'))  # should return False
print(has_unique_chars(''))  # should return True
print(has_unique_chars('0123456789'))  # should return True
print(has_unique_chars('abacadaeaf'))  # should return False
