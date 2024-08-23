def bubble_sort(my_list):
    # starting from the length of the list -1, going all the way to 0,
    # reducing the value by -1 each time
    # moves backward through the list
    for i in range(len(my_list) - 1, 0, -1):
        # moves forward through the list
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                # temp = my_list[j]
                # my_list[j] = my_list[j + 1]
                # my_list[j + 1] = temp
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list


def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    return my_list


def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


print("---------Bubble Sort----------")
print(bubble_sort([4, 2, 5, 6, 1, 3]))
print("\n---------Selection Sort----------")
print(selection_sort([4, 2, 6, 5, 1, 3]))
print("\n---------Insertion Sort----------")
print(insertion_sort([4, 2, 6, 5, 1, 3]))
