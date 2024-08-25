def find_max_min(param):
    max = param[0]
    min = param[0]

    for i in param[1:]:
        if i > max:
            max = i
        if i < min:
            min = i
    return (max, min)


print(find_max_min([5, 3, 8, 1, 6, 9]))

"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)

"""
