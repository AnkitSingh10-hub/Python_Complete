class Employee:
    increment = 1.5

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increase(self):
        self.salary = int(self.salary * self.increment)

    @classmethod
    def change_increment(cls):
        cls.increment = 2

    @staticmethod
    def sum(a, b):
        print(a + b)


e = Employee('Ankit', 'Singh', 5000)
print(e.salary)
e.increase()
print(e.salary)
Employee.change_increment()
e.increase()
print(e.salary)
e.sum(10, 20)
Employee.sum(1, 2)
