# looping through dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(x)

print("\n")

for x in thisdict:
    print(thisdict[x])

print("\n")

for x in thisdict.keys():
    print(x)

print("\n")

for x in thisdict.values():
    print(x)

print("\n")

for x in thisdict.items():
    print(x)

print("\n")

dict_123 = {
    'a': {'x': 1, 'y': 2},
    'b': {'z': 3, 'w': 4},
    'c': [1, 2, 3],
    'd': (1, 2, 3),
}

print(dict_123.values())

print("\n Dictionary comprehesion")
# dictionary comprehension
my_list = [2, 3, 5, 7, 11]

squared_dict = {x: x ** 2 for x in my_list}
print(squared_dict)
