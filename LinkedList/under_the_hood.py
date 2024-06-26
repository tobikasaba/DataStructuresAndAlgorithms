head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": {
                    "value": 4,
                    "next": None
                }
            }
        }
    }
}
# prints out number 23.
# the second next has a nested dictionary with key "value" and its value is 23
print(head["next"]["next"]["value"])

# the syntax for a linked list
# print(my_linked_list.head.head.next.next.value)
