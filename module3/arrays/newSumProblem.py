def find_two_sum(list, target):
    left_index = 0
    right_index = len(list) - 1
    while left_index <= right_index:
        sum = list[left_index] + list[right_index]
        if sum == target:
            return [list[left_index], list[right_index]]
        elif sum < target:
            left_index += 1
        else:
            right_index -= 1
    return []
            
list1 = [-2, 1, 2, 4, 7, 11]
print(find_two_sum(list1, 20))
print(find_two_sum(list1,13))