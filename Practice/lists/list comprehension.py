fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist, "\n")

newlist_2 = [x for x in range(10, 20) if x < 15]
print(newlist_2, "\n")

vegetables = ['carrot', 'raddish', 'spinach']
newlist_3 = [x for x in vegetables]
print(newlist_3, "\n")

num = [1, 2, 3, 4, 5]

num1 = [x ** 2 for x in num]
print(num1)
