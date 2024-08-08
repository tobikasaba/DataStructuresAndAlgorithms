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
        if self.root is None:
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

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def __delete_node(self, current_node, value):
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node

    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)


print("------------Inserting a node-------------")
my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)

print("Root: ", my_tree.root.value)
print("Root -> Left: ", my_tree.root.left.value)
print("Root -> Right: ", my_tree.root.right.value)

print("\n-------Deleting a node--------------")
my_tree.delete_node(2)
print("Root: ", my_tree.root.value)
print("Root -> Left: ", my_tree.root.left.value)
print("Root -> Right: ", my_tree.root.right)

print("\n------------Checking a tree contains a node-------------")
my_tree = BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

print("BST Contains 27: ")
print(my_tree.r_contains(27))

print("\nBST Contains 17: ")
print(my_tree.r_contains(17))

print("\n----------Searching for minimum value---------------")
# the minimum value for the entire tree
print(f"The minimum value for this tree is: {my_tree.min_value(my_tree.root)}")

# the minimum value for the tree on the right-hand side of the root node
print(f"\nThe minimum value for the sub tree is: {my_tree.min_value(my_tree.root.right)}")
