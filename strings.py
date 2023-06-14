string = "Hello World"

print(len(string))
print("\n Indexing :-")

print(string[0])
print("\n Looping through the elements :-")

for i in string:
    print(i)

print("\n Slicing and Indexing :-")
print(string[0:2])
print("\n Slicing and Indexing reverse :-")

string_one = "HelloWorld"
print(string_one[-5:-2])

print("\n String methods :-")

string_two = "There is a white space here"
print(string_two.upper())
print(string_two.lower())
print(string_two.strip())

print(string_two.split())
print(''.join(string_two))

print("\n Something exists in string :-")
if "is" in string_two:
    print(True)
else:
    print(False)
