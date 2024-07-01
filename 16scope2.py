def hi():
    def hello():
        def x():
            print("hi")

        return x()


hi()
