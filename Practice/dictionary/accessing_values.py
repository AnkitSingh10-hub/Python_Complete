thisdict = {"brand": "Ford", "model": "Mustang", "Year": 1964}
print(thisdict, "\n")

# accessing values with key
print(thisdict["brand"])
print("\n")


print(thisdict["Year"])
print("\n")

# printing length of dictionary
print(len(thisdict))
print("\n")

thisdict_1 = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

print(thisdict_1, "\n")

# accessing value with get() method
print(thisdict_1.get("colors"), "\n")
print(thisdict_1.get("A"), "\n")

