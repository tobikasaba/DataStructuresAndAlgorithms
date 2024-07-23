def group_anagrams(strings):
    anagram_groups = {}
    # loops through each string in the string list
    for string in strings:
        # for each string, its sorts the word into a list and then joins that list into a single string in the
        # variable canonical
        canonical = ''.join(sorted(string))
        # if the canonical string isn't in the dictionary, add it to the dictionary
        # with the sting word in a list as the value
        # if it is, append the string word to the list
        if canonical in anagram_groups:
            anagram_groups[canonical].append(string)
        else:
            anagram_groups[canonical] = [string]
    return list(anagram_groups.values())


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print("-----------------")
print(group_anagrams(["c", "d", "q", ]))
