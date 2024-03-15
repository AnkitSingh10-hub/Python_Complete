def add(a, b):
    summation = a + b
    return summation


d = add(10, 20)
print(d)

f = add

print(f(10, 50))


def add(a, b, c):
    print(f"{a}{b}{c}")


add(1, 2, 3)
