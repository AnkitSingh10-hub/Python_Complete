esum = 0
osum = 0
ecount = 0
ocount = 0
for i in range(1, 11):
    if i % 2 == 0:
        esum = esum + i
        ecount = ecount + 1
    else:
        osum = osum + i
        ocount = ocount + 1

print(f"Odd sum = {osum} and count = {ocount}")
print(f"Even sum = {esum} and count = {ecount}")
