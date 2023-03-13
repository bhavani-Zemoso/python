class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    
    def insert_after_node(self, position, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        prev = None
        for i in range(1, position):
            if temp is None:
                print("Invalid position")
                return
            prev = temp
            temp = temp.next

        prev.next = new_node
        new_node.next = temp

    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return
        
        curr_node = self.head
        if curr_node.data == value:
            self.head = curr_node.next
            curr_node = None
            return
        
        prev = None

        while curr_node and curr_node.data != value:
            prev = curr_node
            curr_node = curr_node.next
        
        prev.next = curr_node.next
        curr_node = None

    def delete_by_position(self, position):
        if self.head is None:
            print("List is empty")
            return
        
        curr_node = self.head
        if position == 1:
            self.head = curr_node.next
            curr_node = None
            return
        
        prev = None

        for i in range(1, position):
            if curr_node is None:
                print("Invalid position")
                return
            prev = curr_node
            curr_node = curr_node.next
        
        prev.next = curr_node.next
        curr_node = None

    def length_of_list(self):
        if self.head is None:
            print("List is empty")
            return
        
        count = 0
        curr_node = self.head
        while curr_node:
            count = count + 1
            curr_node = curr_node.next
        
        return count
    
    def recursive_length(self, node):
        if node is None:
            return 0
        return 1 + self.recursive_length(node.next)
    
    def reverse_iterative(self):
        prev = None 
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 
        self.head = prev
    
    def merge_sorted(self, llist):

        p = self.head 
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p 
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s 
        while p and q:
            if p.data <= q.data:
                s.next = p 
                s = p 
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q 
        if not q:
            s.next = p

        self.head = new_head     
        return self.head
    
    def remove_duplicates(self):
        
        cur = self.head
        prev = None

        dup_values = dict()

        while cur:
            if cur.data in dup_values:
                # Remove node:
                prev.next = cur.next
                cur = None
            else:
                # Have not encountered element before.
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next

    def rotate(self, k):
        if self.head and self.head.next:
            p = self.head 
            q = self.head 
            prev = None
            count = 0
            
            while p and count < k:
                prev = p
                p = p.next 
                q = q.next 
                count += 1
            p = prev
            while q:
                prev = q 
                q = q.next 
            q = prev 

            q.next = self.head 
            self.head = p.next 
            p.next = None


linked_list = LinkedList()
linked_list.append("A")
linked_list.append("B")
linked_list.prepend("C")
linked_list.prepend("D")
linked_list.insert_after_node(3, "E")
linked_list.print_list()
print(linked_list.length_of_list())

print("")

linked_list.delete_by_value("D")
linked_list.print_list()
print(linked_list.length_of_list())

print("")
linked_list.delete_by_position(4)
linked_list.print_list()
print(linked_list.length_of_list())

print(linked_list.recursive_length(linked_list.head))
