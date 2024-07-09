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
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def reverse(self):
        if self.head is None:
            return None
        current_node = self.head
        before = current_node.prev
        after = current_node.next
        temp = current_node
        for _ in range(self.length):
            if temp.next is not None:
                temp = temp.next
            current_node.prev = after
            current_node.next = before
            current_node = temp
            after = current_node.next
            before = current_node.prev

        self.tail = self.head
        self.head = temp


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)

print('DLL before reverse():')
my_doubly_linked_list.print_list()

my_doubly_linked_list.reverse()

print('\nDLL after reverse():')
my_doubly_linked_list.print_list()
