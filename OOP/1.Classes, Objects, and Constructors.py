class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary


e = Employee('Ankit', 'Singh', 5000)

print(e.fname)
print(e.lname)
print(e.salary)
