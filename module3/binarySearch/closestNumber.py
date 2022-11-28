def closest_number(list, target):
    if list is None:
        return None
    if len(list) == 1:
        return list[0]
    low = 0
    high = len(list) - 1
    closest_value = list[0]

    while low <= high:
        mid = (low + high) // 2
        diff = abs(target - list[mid])
        if abs(closest_value - target) > diff:
            closest_value = list[mid]
        if target < list[mid]:
            high = mid - 1
        elif target > list[mid]:
            low = mid + 1
    
    return closest_value

list = [1, 2, 4, 5, 6, 6, 8, 9]
print(closest_number(list, 11))

list = [2, 5, 6, 7, 8, 8, 9]
print(closest_number(list, 4))
