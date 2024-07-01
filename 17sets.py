# A set is a collection which is unordered(not indexed), unchangeable(immutable), no duplicate values
# Set items are unchangeable, but you can remove items and add new items.
a = {1, 2, 3, 3, 1, 2}
print(a)

print("\n")
b = {'a', 'b', 'c'}
print(b)
print("\n")
c = b.union(a)
print(c)
