def func(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs.get('a'))


func(1, 2, 3, 4, a=1999, b=2000)
