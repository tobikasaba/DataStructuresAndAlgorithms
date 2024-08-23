class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def merge(self, other_list):
        starting_point = Node(0)
        current_node = starting_point
        list_1 = self.head
        list_2 = other_list.head

        while list_1 is not None and list_2 is not None:
            if list_1.value < list_2.value:
                current_node.next = list_1
                list_1 = list_1.next
            else:
                current_node.next = list_2
                list_2 = list_2.next
            current_node = current_node.next

        if list_1 is not None:
            current_node.next = list_1

        else:
            current_node.next = list_2
            self.tail = other_list.tail

        self.length += other_list.length


l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)

l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""
