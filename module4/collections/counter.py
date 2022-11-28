from collections import Counter

counter1 = Counter("super")
counter2 = Counter("superfluous")

print(counter1)
print(counter2)

print(counter1.elements())
print(counter2.elements())

print(counter1.most_common(2))
print(counter2.most_common(3))

print(counter1.subtract(counter2))