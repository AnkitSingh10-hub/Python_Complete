from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# This will raise an error because you can't instantiate an abstract class
try:
    animal = Animal()
except TypeError as e:
    print(e)

# Correct usage
dog = Dog()
print(dog.make_sound())  # Output: Bark

cat = Cat()
print(cat.make_sound())  # Output: Meow
