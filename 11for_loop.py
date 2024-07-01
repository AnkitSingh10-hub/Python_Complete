fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

print("Getting even numbers \n")
for x in range(2, 20, 2):
    print(x)

print("Getting reverse numbers \n")

for x in range(10, 0, -1):
    print(x)

print("Getting nested loop \n")

for i in range(0, 11):
    for j in range(0, 11):
        print(i, j)

print("Getting list comprehesion \n")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x == "apple"]
print(newlist)
