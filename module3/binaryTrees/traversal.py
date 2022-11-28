from queue import Queue, LifoQueue

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)
    
    def pre_order_traversal(self, start, traversal):
        if start:
            traversal += (str(start.value) + " - ")
            traversal = self.pre_order_traversal(start.left, traversal)
            traversal = self.pre_order_traversal(start.right, traversal)
        return traversal
    
    def post_order_traversal(self, start, traversal):
        if start:
            traversal = self.post_order_traversal(start.left, traversal)
            traversal = self.post_order_traversal(start.right, traversal)
            traversal += (str(start.value) + " - ")
        return traversal
    
    def inorder_traversal(self, start, traversal):
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value) + " - ")
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal
    
    def level_order_traversal(self, root, traversal):
        queue = Queue()
        queue.put(root)
        while queue.empty() is not True:
            curr_node = queue.get()
            traversal += (str(curr_node.value) + " - ")
            if curr_node.left:
                queue.put(curr_node.left)
            if curr_node.right:
                queue.put(curr_node.right)
        return traversal
    
    def reverse_level_order_traversal(self, root, traversal):
        queue = Queue()
        stack = LifoQueue()
        queue.put(root)
        while queue.empty() is not True:
            curr_node = queue.get()
            stack.put(curr_node.value)
            if curr_node.right:
                queue.put(curr_node.right)
            if curr_node.left:
                queue.put(curr_node.left)

        while stack.empty() is not True:
            traversal += (str(stack.get()) + " - ")

        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.pre_order_traversal(tree.root, ""))
print(tree.post_order_traversal(tree.root, ""))
print(tree.inorder_traversal(tree.root, ""))
print(tree.level_order_traversal(tree.root, ""))
print(tree.reverse_level_order_traversal(tree.root, ""))


