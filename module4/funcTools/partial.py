from functools import partial
def add(x, y):
    return x + y

p_add = partial(add, 2)
print(p_add(4))

print(p_add(5))
