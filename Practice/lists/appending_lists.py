# appending list items at the back of the list
appending_list = [1, 2, 3, 4, 5]
print(appending_list)
appending_list.append("ANKIT")
print(appending_list)
appending_list.insert(1, "SINGH")
print(appending_list)

colors = ["red", "green"]
more_colors = ["blue", "yellow"]
all_colors = colors + more_colors
print(all_colors)

sum = [1, 2, 3]
sum.append([4, 8])
sum.insert(0, [4])

print(f"{sum}")
