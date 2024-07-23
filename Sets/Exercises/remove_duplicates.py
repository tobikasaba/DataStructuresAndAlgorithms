def remove_duplicates(my_list):
    no_duplicates_list = set()
    for number in my_list:
        no_duplicates_list.add(number)

    return list(no_duplicates_list)


my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
new_list = remove_duplicates(my_list)
print(new_list)
