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

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        # set the last value in the heap as the head of the heap
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]):
                max_index = left_index
            if (right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]):
                max_index = right_index
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return


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
print("------------------")
my_heap = MaxHeap()
my_heap.insert(95)
my_heap.insert(75)
my_heap.insert(80)
my_heap.insert(55)
my_heap.insert(60)
my_heap.insert(50)
my_heap.insert(65)
print(my_heap.heap)
my_heap.remove()
print(my_heap.heap)
my_heap.remove()
print(my_heap.heap)
