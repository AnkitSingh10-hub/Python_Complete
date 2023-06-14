class Item:
    # __name is private instance variables
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    # public getter
    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    # public setter
    @name.setter
    def name(self, value):
        self.__name = value

    @price.setter
    def price(self, value):
        self.__price = value

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value


i = Item('Mobile', 700, 10)
print(i.name, i.price, i.quantity)

i.name = "Ankit"
i.price = 100
i.quantity = 5
print(i.name, i.price, i.quantity)
