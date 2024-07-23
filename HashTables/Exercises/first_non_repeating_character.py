def first_non_repeating_char(string):
    my_dict = {}
    for char in string:
        if char not in my_dict:
            my_dict[char] = 1
        else:
            my_dict[char] += 1
    for char in my_dict:
        if my_dict[char] == 1:
            return char
    return None


print(first_non_repeating_char('leetcode'))

print(first_non_repeating_char('hello'))

print(first_non_repeating_char('aabbcc'))
