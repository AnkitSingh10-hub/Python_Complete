def func(a, b, c):
    print(f"{a} {b} {c}")


func(b="Ankit", c="Singh", a=500)


def func_1(**kwargs):
    for i in kwargs.items():
        print(i)
    print(kwargs)
    print(kwargs['a'])
    print(kwargs['d'])


func_1(b=1, a=2, c=3, d="4th element")
