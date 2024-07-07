class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True

    def reverse_between(self, start_index, end_index):
        # return None if the linked list is empty or has only one node
        if self.head is None or self.length == 1:
            return None

        dummy_node = Node(0)
        dummy_node.next = self.head
        prev_node = dummy_node

        for _ in range(start_index):
            prev_node = prev_node.next

        current_node = prev_node.next

        for _ in range(end_index - start_index):
            node_to_move = current_node.next
            current_node.next = node_to_move.next
            node_to_move.next = prev_node.next
            prev_node.next = node_to_move

        self.head = dummy_node.next
        # # break_point = None
        # # start_node = None
        # # end_node = None
        # # prev_node = None
        # # current_node = self.head
        # # after = current_node.next
        #
        #
        #
        # for i in range(self.length):
        #     if i == start_index:
        #         start_node = current_node
        #     elif i == end_index:
        #         end_node = current_node
        #
        #     # else:
        #     #     break_point = current_node
        #     prev_node = current_node
        #     current_node = current_node.next
        #
        # for i in range(start_index, end_index+1)
        #     start_index


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()
