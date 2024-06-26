class Employee:
    increment = 1.5

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increment = 1.0

    def increase(self):
        self.salary = int(self.salary * Employee.increment)


e = Employee('Ankit', 'Singh', 5000)

print(e.salary)
e.increase()
print(e.salary)
print(e.increment)
