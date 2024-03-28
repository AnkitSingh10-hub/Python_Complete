def func(**kwargs):
    print(kwargs)
    for i in kwargs:
        print(i)


dic = {'a': 2, 'b': 3, 'c': 100}

func(**dic)
