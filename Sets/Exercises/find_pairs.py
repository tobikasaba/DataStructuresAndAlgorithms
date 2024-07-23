def find_pairs(arr1, arr2, target):
    set1 = set(arr1)
    pairs_list = []
    for number in arr2:
        complement = target - number
        if complement in set1:
            pairs_list.append((complement, number))
    return pairs_list


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print(pairs)
