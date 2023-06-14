x = 100


def func():
    print(x)


def func1():
    global x
    x = x + 100
    print(x)


def func2():
    x = 2
    print(x)


func()
func1()
func2()
