class Student:
    def __init__(self, name, roll, address):
        self.__name = name
        self.__roll = roll
        self.__address = address

    @property
    def name(self):
        return self.__name

    @property
    def roll(self):
        return self.__roll

    @property
    def address(self):
        return self.__address

    @name.setter
    def name(self, value):
        self.__name = value

    @roll.setter
    def roll(self, value):
        self.__roll = value

    @address.setter
    def address(self, value):
        self.__address = value


s = Student("Ankit", 181651, "Chhauni")
print(s.name, s.roll, s.address)

s.name = "Hi"
s.roll = 1
s.address = "Nepal"
print(s.name, s.roll, s.address)
