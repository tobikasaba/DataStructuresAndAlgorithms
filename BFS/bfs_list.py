from Trees.constructor import BinarySearchTree


def BFS(self):
    current_node = self.root
    queue = []
    results = []
    queue.append(current_node)

    while len(queue) > 0:
        current_node = queue.pop(0)
        results.append(current_node.value)
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)
    return results


# this essentially makes the BFS function a method of the BinarySearchTree class even though it is defined outside it
BinarySearchTree.BFS = BFS

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.BFS())
