list_1 = ["A", "B", "C"]
s_1 = "Javatpoint"
# creating enumerate objects

print(list(enumerate(list_1)))
print(list(enumerate(s_1)))

names = ["Alice", "Bob", "Charlie", 100]
ages = [25, 30, 35, 100]
scores = (85, 92, 88, 44)
# Combining the lists using zip()
combined = zip(names, ages, scores)


# Iterating over the combined iterable
for item in combined:
    print(item)
