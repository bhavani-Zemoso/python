class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)
    
    def calculate_height(self, node):
        if node is None:
            return -1
        left_height = self.calculate_height(node.left)
        right_height = self.calculate_height(node.right)
        return 1 + max(left_height, right_height)

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.left.left.left = Node(6)
tree.root.left.left.left.left = Node(7)

print(tree.calculate_height(tree.root))
print(tree.calculate_height(tree.root.right))
