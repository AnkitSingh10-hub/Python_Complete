class Animal:
    def speak(self):
        print("Speak")


class Cat(Animal):
    def speak(self):
        print("Meow")


class Dog(Animal):
    def speak(self):
        print("Woof")


c = Cat()
d = Dog()

c.speak()
d.speak()
