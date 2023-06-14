def func1(func):
    print("Decorator Invoked")
    func(10, 12)


@func1
def func(a, b):
    print(a + b)
