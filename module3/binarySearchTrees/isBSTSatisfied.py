from queue import Queue
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root_value):
        self.root = Node(root_value)
    
    def insert(self, node, value):
        if value <= node.value:
            if node.left is None:
                new_node = Node(value)
                node.left = new_node
            else:
                self.insert(node.left, value)
        else:
            if node.right is None:
                new_node = Node(value)
                node.right = new_node
            else:
                self.insert(node.right, value)
    
    def is_bst_satisfied(self):
        queue = Queue()
        queue.put(self.root)
        while queue.empty() is not True:
            curr_node = queue.get()
            if curr_node.left:
                if curr_node.value > curr_node.left.value:
                    queue.put(curr_node.left)
                else:
                    return False
            if curr_node.right:
                if curr_node.value < curr_node.right.value:
                    queue.put(curr_node.right)
                else:
                    return False
        return True

list = [23,78,12,3,9,89,56,32]
search_tree = BinarySearchTree(list[0])
list = list[1:]
for number in list:
    search_tree.insert(search_tree.root, number)

print(search_tree.is_bst_satisfied())

tree = BinarySearchTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.left.left.left = Node(6)
tree.root.left.left.left.left = Node(7)

print(tree.is_bst_satisfied())

