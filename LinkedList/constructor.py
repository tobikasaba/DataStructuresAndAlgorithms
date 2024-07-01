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
        # if self.length is = 0 after popping the last value
        if self.length == 0:
            popped_node = temp
            self.head = None
            self.tail = None
        return popped_node.value

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            # self.head = None # this is redundant because there is only one node in the list,
            # and we have yet set the value of head to none earlier
            self.tail = None
        return temp

    def prepend(self, value):
        # create a new node
        new_node = Node(value)

        # add Node to the beginning
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.tail.next = None
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        # temp = self.head
        # prev = self.head
        # counter = 0
        # while counter != index:
        #     prev = temp
        #     temp = temp.next
        #     counter += 1
        # return prev

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        # if index < 0 or index >= self.length:
        #     return None
        # temp = self.head
        # for i in range(index + 1):
        #     if i == index:
        #         temp.value = value
        #         return True
        #     temp = temp.next

        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        # this allows for index == to the length because the last node at (index-1) points to none
        if index < 0 or index > self.length:
            return False
        if index == 0:
            # i.e. linkedlist.prepend hence running it on the particular instance of linked list
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        print("length", self.length)
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next  # more efficient than using self.get(index)
        prev.next = temp.next  # more efficient than using self.get(index + 1)
        temp.next = None
        self.length -= 1
        return temp

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


test = LinkedList(2)
test.append(3)
test.prepend(1)
test.insert(1, 1.5)
test.print_list()
print("---------------")
print(test.remove(2))
test.print_list()
