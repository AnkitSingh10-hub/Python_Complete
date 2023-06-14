class A:
    def __init__(self):
        print("Hello I just returned a class")


def func():
    return A()


func()
