class Animal:
    @property
    def add(self):
        print("add")

    @property
    def subtract(self):
        print("subtract")


a = Animal()
a.add
a.subtract
