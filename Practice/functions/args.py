def my_func(*args):
    for i in args:
        print(i)
    print("first item =", args[0])
    print(args)


my_func("Ankit you are good", 1, 2, 3)

print("\n")


def my_func2(*args):
    print(args)
    print(args[0])


my_func2(1, 2, 3, 4, 5, 6)
