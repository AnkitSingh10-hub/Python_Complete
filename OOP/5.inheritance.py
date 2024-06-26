class Employee:
    increment = 2

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increase(self):
        self.salary = int(self.salary * self.increment)

    @classmethod
    def change_increment(cls):
        cls.increment = 2
        print("It called")

    @staticmethod
    def sum(a, b):
        print(a + b)


class Programmer(Employee):
    def __init__(self, fname, lname, salary, proglag, exp):
        super().__init__(fname, lname, salary)
        self.proglag = proglag
        self.exp = exp

    def increase(self):
        super().increase()


p = Programmer('Ram', 'Singh', 5000, 'Python', 'Junior')
print(p.fname, p.lname, p.salary, p.proglag, p.exp)
p.increase()
print(p.salary)
Employee.change_increment()
Employee.sum(1,1)
