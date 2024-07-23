def find_duplicates(nums):
    my_dict = {}
    duplicates = []
    for number in nums:
        if number in my_dict:
            duplicates.append(number)
        else:
            my_dict[number] = True
    return duplicates
