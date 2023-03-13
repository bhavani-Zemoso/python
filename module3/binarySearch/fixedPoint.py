def find_fixed_point(list):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        if mid == list[mid]:
            return mid
        elif mid > list[mid]:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

list = [-10, -5, 0, 2, 90]
print(find_fixed_point(list))