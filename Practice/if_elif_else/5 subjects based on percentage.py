marks = int(input("Enter marks"))

if marks >= 80:
    print("Distinction")
elif 60 <= marks < 80:
    print("First division")
elif 45 <= marks < 60:
    print("Second division")
elif 32 <= marks < 45:
    print("Third division")
else:
    print("Failed")
