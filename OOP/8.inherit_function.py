class A:
    def call(self):
        print("Hi")


class B(A):
    def func(self):
        return self.call()


b = B()
b.func()
