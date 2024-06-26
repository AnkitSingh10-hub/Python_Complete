class Person:
    def __init__(self, name, roll):
        self.__name = name
        self.__roll = roll


p = Person('Ankit', 11)
print(p.__name, p.__roll)
