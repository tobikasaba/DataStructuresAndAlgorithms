class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


def sort_stack(my_stack):
    sorted_stack = Stack()
    # this loop runs until the inout stack is empty.
    # when this loop breaks, the sorted_stack will have a sorted list of numbers
    while my_stack.is_empty() is False:
        temp = my_stack.pop()
        while sorted_stack.is_empty() is False and sorted_stack.peek() > temp:
            my_stack.push(sorted_stack.pop())
        sorted_stack.push(temp)

    # the values of the sorted my_stack are then added to the input stack in reverse
    while sorted_stack.is_empty() is False:
        my_stack.push(sorted_stack.pop())


my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()

"""
    EXPECTED OUTPUT:
    ----------------
    Stack before sort_stack():
    2
    4
    5
    1
    3

    Stack after sort_stack:
    1
    2
    3
    4
    5

"""
