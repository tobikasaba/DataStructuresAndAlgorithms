class LinkedList:
    # each node is an instance of new node which has a value and next attribute.
    # this makes setting the next value of each node possible
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
            # this sets the pointer of the current node to the new node being added
            self.tail.next = new_node
            # this then sets the tail of the linked list to the new node being added
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        prev = self.head
        temp = self.head
        if self.length == 0:
            return None
        while temp.next is not None:
            prev = temp
            temp = temp.next
        popped_node = temp
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            popped_node = temp
            self.head = None
            self.tail = None
        return popped_node.value

    def prepend(self, value):
        # create a new node
        new_node = Node(value)
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
            # sets the value of temp to the value the next attribute specified in a node,
            # for example, when a new node is instantiated, the value of the node is specified
            # and the value of the next attribute
            temp = temp.next


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


test = LinkedList(1)
test.append(2)
test.print_list()
print("---------")
print("Popped value is ", test.pop())
print("Popped value is", test.pop())
test.print_list()
