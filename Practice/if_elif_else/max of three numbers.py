a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))

if a > b and a > c:
    print(f"a is the greatest and value is {a}")
elif b > a and b > c:
    print(f"b is the greatest and value is {b}")
else:
    print(f"c is the greatest and value is {c}")
