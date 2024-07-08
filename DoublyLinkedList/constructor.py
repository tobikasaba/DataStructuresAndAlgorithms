class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            self.head.prev = None
            temp.next = None

        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index > self.length // 2:
            temp = self.tail
            # for _ in range((self.length - 1) - index):
            # this tells the for loop to decrease by one
            # essentially starting the loop from the end of the linkedlist
            # e.g. if length = 10 and index = 3
            # range (9, 6) decreasing by one so its 9,8,7
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_dll = DoublyLinkedList(7)
my_dll.append(3)
my_dll.append(5)
my_dll.print_list()
my_dll.prepend(2)
print("-------")
my_dll.print_list()
my_dll.pop()
print("-------")
my_dll.print_list()
print("-------")
my_dll.pop_first()
my_dll.print_list()

second_dll = DoublyLinkedList(6)
second_dll.append(7)
second_dll.append(8)
second_dll.append(4)
second_dll.append(5)
print("-------")
print(second_dll.get(4))
print("-------")
second_dll.insert(3, 18)
second_dll.print_list()
