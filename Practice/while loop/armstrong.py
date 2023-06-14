num = int(input("Enter a number"))
sum = 0
rem = 0
original_number = num

while num > 0:
    rem = num % 10
    sum = int(sum + rem * rem * rem)
    num = int(num / 10)


if original_number == sum:
    print("The number is armstrong")
else:
    print("The number is not armstrong")
