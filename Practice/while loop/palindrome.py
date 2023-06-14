num = int(input("Enter a number"))
rev = 0
rem = 0

original_num = num


while num > 0:
    rem = num % 10
    rev = int(rev * 10 + rem)
    num = int(num / 10)


print(f"The reversal is {rev}")

if original_num == rev:
    print("It is palindrome")
else:
    print("It is not palindrome")