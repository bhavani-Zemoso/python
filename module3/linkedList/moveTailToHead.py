def move_tail_to_head(self):
    last_node = self.head
    prev = None
    while last_node.next:
        prev = last_node
        last_node = last_node.next
    
    prev.next = None
    last_node.next = self.head
    self.head = last_node