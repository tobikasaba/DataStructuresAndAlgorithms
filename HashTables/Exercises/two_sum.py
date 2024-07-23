def two_sum(nums, target):
    # create an empty hash table
    num_map = {}

    # iterate through each number in the array
    for i, num in enumerate(nums):
        # calculate the complement of the current number
        complement = target - num

        # check if the complement is in the hash table
        if complement in num_map:
            # if it is, return the indices of the two numbers
            return [num_map[complement], i]

        # add the current number and its index to the hash table
        num_map[num] = i
        print(num_map)
    # if no two numbers add up to the target, return an empty list
    return []


print(two_sum([5, 1, 7, 2, 9, 3], 10))
print(two_sum([3, 3], 6))
