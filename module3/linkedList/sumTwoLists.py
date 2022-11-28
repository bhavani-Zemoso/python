def sum_two_lists(self, llist):

    carry = 0
    list1_node = llist.head
    list2_node = self.head

    sum_list = LinkedList()

    while list1_node and list2_node:
        sum = list1_node.data + list2_node.data + carry
        remainder = sum
        carry = 0
        if sum >= 10:
            remainder = sum % 10
            carry = sum // 10

        sum_list.append(remainder)
        list1_node = list1_node.next
        list2_node = list2_node.next
    
    while list1_node:
        sum = list1_node.data
        if carry != 0:
            sum += carry
            carry = 0
        sum_list.append(sum)
        list1_node = list1_node.next
    
    while list2_node:
        sum = list2_node.data
        if carry != 0:
            sum += carry
            carry = 0
        sum_list.append(sum)
        list2_node = list2_node.next
    
    return sum_list
            
        
