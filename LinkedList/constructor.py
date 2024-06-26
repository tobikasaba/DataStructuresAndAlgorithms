class LinkedList:
    def __init__(self, value):
        # create a new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        # create a new node
        new_node = Node(value)
        # add Node to the end
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            # this sets the pointer of the current node to the new node
            self.tail.next = new_node
            # this then sets the tail of the linked list to the new node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        # create a new node
        # add Node to the beginning
        pass

    def insert(self, index, value):
        # create a new node
        # insert the node at a desired index
        pass

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
