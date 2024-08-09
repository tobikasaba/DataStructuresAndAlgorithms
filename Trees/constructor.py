class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    # def __init__(self, value):
    #     new_node = Node(value)
    #     self.root = new_node

    # creating a BST where there is no value included
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root

        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False


if __name__ == "__main__":
    my_tree = BinarySearchTree()
    print(my_tree.root)
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)
    print(f"The root value is: {my_tree.root.value}")
    print(f"The value to the left of root is: {my_tree.root.left.value}")
    print(f"The value to the right of root is: {my_tree.root.right.value}")
    print("--------------------")
    print(my_tree.contains(27))

    print(my_tree.contains(17))
