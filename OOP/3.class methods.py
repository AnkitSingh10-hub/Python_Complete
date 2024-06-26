class Employee:
    increment = 1.5

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increase(self):
        self.salary = int(self.salary * self.increment)

    @classmethod
    def changeincrement(cls):
        cls.increment = 2


e = Employee("Ankit", "Singh", 5000)
print(e.salary)
e.increase()
print(e.salary)
Employee.changeincrement()
e.increase()

print(e.salary)
