class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __r_contains(self, current_node, value):
        if current_node is None:
            return False

        if value == current_node.value:
            return True

        if value < current_node.value:
            return self.__r_contains(current_node.left, value)

        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)


my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)

print("Root: ", my_tree.root.value)
print("Root -> Left: ", my_tree.root.left.value)
print("Root -> Right: ", my_tree.root.right.value)

print("-------------------------")

my_tree = BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(82)
my_tree.r_insert(52)

print("BST Contains 27: ")
print(my_tree.r_contains(27))

print("\nBST Contains 17: ")
print(my_tree.r_contains(17))
