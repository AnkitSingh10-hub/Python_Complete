num = int(input("Enter a number"))
rem = 0
rev = 0

while num > 0:
    rem = num % 10
    rev = int(rev * 10 + rem)
    num = int(num / 10)


print(f"The reversal is {rev}")