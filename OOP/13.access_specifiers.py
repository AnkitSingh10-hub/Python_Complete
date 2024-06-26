class MyClass:
    def __init__(self):
        self.public_var = "I am public"
        self._protected_var = "I am protected"
        self.__private_var = "I am private"

    def public_method(self):
        return "This is a public method"

    def _protected_method(self):
        return "This is a protected method"

    def __private_method(self):
        return "This is a private method"

# Create an instance of MyClass
obj = MyClass()

# Accessing public variable and method
print(obj.public_var)  # Output: I am public
print(obj.public_method())  # Output: This is a public method

# Accessing protected variable and method
print(obj._protected_var)  # Output: I am protected
print(obj._protected_method())  # Output: This is a protected method

# Attempting to access private variable and method directly will result in an AttributeError
# print(obj.__private_var)  # This will raise an AttributeError
# print(obj.__private_method())  # This will raise an AttributeError

# Accessing private variable and method using name mangling
print(obj._MyClass__private_var)  # Output: I am private
print(obj._MyClass__private_method())  # Output: This is a private method
