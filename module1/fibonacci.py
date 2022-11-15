def fibonacci(n):
    if n <= 0:
        return -1
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    first = 0
    second = 1
    for i in range(3, n):
        third = first + second
        first = second
        second = third
    
    return first + second

print(fibonacci(2))