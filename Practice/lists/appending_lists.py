# appending list items at the back of the list
appending_list = [1, 2, 3, 4, 5]
print(appending_list)
appending_list.append("ANKIT")
print(appending_list)
appending_list.insert(0, "SINGH")
print(appending_list)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

tropical_tuple = ("strawberry", "grape")
thislist.extend(tropical_tuple)

print(thislist)

sum = [1, 2, 3]
sum.append([4, 8])
sum.insert(0, [4])

print(f"{sum}")
