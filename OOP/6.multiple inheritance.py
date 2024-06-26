class A:
    def print(self):
        print("Hello World A")


class B:
    def print(self):
        print("Hello World B")


class C(A, B):
    def print(self):
        super().print()

        print("Hello World C")


c = C()
c.print()
