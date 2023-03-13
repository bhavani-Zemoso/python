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

    def search(self, node, value):
        if node is None:
            return False
        elif node.value == value:
            return True
        elif node.value > value:
            return self.search(node.left, value)
        elif node.value < value:
            return self.search(node.right, value)
        
        

list = [23,78,12,3,9,89,56,32]
search_tree = BinarySearchTree(list[0])
list = list[1:]
for number in list:
    search_tree.insert(search_tree.root, number)

print(search_tree.search(search_tree.root, 32))
print(search_tree.search(search_tree.root, 1000))



