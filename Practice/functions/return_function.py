def hello():
    print("I can be called")


def hi():
    print("I just called Hello")
    return hello()


hi()
