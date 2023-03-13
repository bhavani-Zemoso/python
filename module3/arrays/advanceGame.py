def array_advance(array):
    furthest_reached = 0
    last_index = len(array) - 1
    i = 0
    while i <= furthest_reached and furthest_reached < last_index:
        furthest_reached = max(furthest_reached, array[i] + i)
        i += 1
    return furthest_reached >= last_index

array1 = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(array1))

array2 = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(array2))