i = 1

while i <= 10:
    print(i)
    i = i + 1
else:
    print("The while loop ended \n")

print("The second loop started \n")

j = 1
while j <= 10:
    print(j)
    if j == 7:
        break
    j = j + 1
else:
    print("Second loop break doesn't happen because the loop didn't fully end")
