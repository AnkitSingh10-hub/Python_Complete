thisdict = {"brand": "Ford", "model": "Mustang", "Year": 1964}

# making a list of keys and a list of values
x = thisdict.keys()
y = thisdict.values()


print(x)
print("\n")

print(y)
print("\n")

for i in thisdict.keys():
    print(i)
print("\n")
for i in thisdict:
    print(i)
print("\n")
for i in thisdict.values():
    print(i)