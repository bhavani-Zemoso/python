def sum_zero(list):
    for number in list:
        if -(number) in list:
            return True
    return False

print(sum_zero([10, -14, 26, 5, -3, 13, -9]))