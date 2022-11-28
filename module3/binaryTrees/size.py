class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def size_of_tree(self, node):
        if node is None:
            return 0
        return 1 + self.size_of_tree(node.left) + self.size_of_tree(node.right)

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.left.left.left = Node(6)
tree.root.left.left.left.left = Node(7)

print(tree.size_of_tree(tree.root))