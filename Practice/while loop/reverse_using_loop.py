string = "Ankit"
reverse = ""
count = len(string)
while count > 0:
    reverse = reverse + string[count-1]
    count = count - 1

print(reverse)
