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


def dfs_pre_order(self):
    results = []

    def traverse(current_node):
        results.append(current_node.value)
        if current_node.left is not None:
            traverse((current_node.left))
        if current_node.right is not None:
            traverse(current_node.right)

    traverse(self.root)
    return results


# this essentially makes the BFS function a method of the BinarySearchTree class even though it is defined outside it
BinarySearchTree.BFS = BFS
BinarySearchTree.dfs_pre_order = dfs_pre_order
my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print("-----------Depth First Search--------")
print(my_tree.BFS())
print("\n-------------PreOrder--------")
print(my_tree.dfs_pre_order())
