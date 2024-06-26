class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call the __init__ method of the parent class with arguments
        self.student_id = student_id

    def introduce(self):
        parent_intro = super().introduce()  # Call the introduce method of the parent class
        return f"{parent_intro} My student ID is {self.student_id}."

# Create an instance of Student
student = Student("Alice", 21, "S12345")

# Call the introduce method
print(student.introduce())  # Output: Hi, I'm Alice and I'm 21 years old. My student ID is S12345.
