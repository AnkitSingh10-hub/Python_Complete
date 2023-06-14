# looping through a list
list_loop_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list_loop_1:
    print(i)

print("\n")
for j in range(len(list_loop_1)):
    print(list_loop_1[j])

print("\n While looping")

i = 0
while i < len(list_loop_1):
    print(list_loop_1[i])
    i = i + 1

# List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)
