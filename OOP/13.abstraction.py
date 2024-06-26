from abc import ABC, abstractmethod


class Parent(ABC):
    @abstractmethod
    def call(self):
        pass


class Child1(ABC):
    def call(self):
        print("Child 1")


class Child2(ABC):
    def call(self):
        print("Child 1")


c1 = Child1()
c2 = Child2()

c1.call()
c2.call()

p = Parent()
p.call()