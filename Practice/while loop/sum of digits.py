num = int(input("Enter a number"))
sum = 0
rem = 0

while num > 0:
    rem = num % 10
    sum = int(sum + rem)
    num = int(num / 10)

print(f"The sum of digits is {sum}")



