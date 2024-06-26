from constructor import LinkedList, Node

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

print("---------------------------")
# the syntax for a linked list
my_linked_list = LinkedList(4)
print(my_linked_list.head.value)
print(my_linked_list.tail.value)

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.print_list()
