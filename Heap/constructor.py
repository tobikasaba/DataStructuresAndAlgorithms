class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        # loop runs as long as the index value is greater than zero hence not at the top
        # and the current node value is greater than its parent node value
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            # swap the current node with its parent node using their indexes
            self._swap(current, self._parent(current))
            # update the value of current to its new position, which is now the parent of the swapped node
            current = self._parent(current)


my_heap = MaxHeap()
my_heap.insert(99)
my_heap.insert(72)
my_heap.insert(61)
my_heap.insert(58)
print(my_heap.heap)
print("------------------")
my_heap.insert(100)
print(my_heap.heap)
print("------------------")
my_heap.insert(75)
print(my_heap.heap)
