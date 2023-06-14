# looping through tuples
tuple_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for i in tuple_1:
    print(i)

print("\n")

for j in range(len(tuple_1)):
    print(tuple_1[j])

print("\n")

k = 0
while k < len(tuple_1):
    print(tuple_1[k])
    k = k + 1

print("\n")

# checking if a certain item exists in a tuple

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple", "\n")

thistuple = ("apple", "banana", "cherry")
del thistuple

# Converting list into tuple and vice versa
a = [1, 2, 3]
b = tuple(a)
print(b)
a = list(b)
print(a)
