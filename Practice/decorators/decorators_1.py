def func1(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")

    return wrapper()


@func1
def func():
    print("I am the argument function")
