# Import the array module
import array

# Create an array of integers
integer_array = array.array('i', [1, 2, 3, 4, 5])

# Accessing elements of the array
print("Array elements:")
for num in integer_array:
    print(num)

# Accessing a specific element
print("Element at index 2:", integer_array[2])

# Modifying an element
integer_array[1] = 10
print("Modified array:", integer_array)

# Finding the length of the array
print("Length of the array:", len(integer_array))

# Adding elements to the array
integer_array.append(6)
integer_array.extend([7, 8, 9])
print("Updated array:", integer_array)

# Removing elements from the array
integer_array.pop(2)
integer_array.remove(5)
print("Array after removal:", integer_array)