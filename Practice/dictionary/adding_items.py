thisdict = {"brand": "Ford", "model": "Mustang", "Year": 1964, "age": 10}

# adding and updating items in dictionary
print(thisdict, "\n")

thisdict.update({"Year": 2020})
print(thisdict, "\n")

thisdict.update({"id": 100})
print(thisdict, "\n")

thisdict["exp"] = "new"

print(thisdict)


thisdict["brand"] = "StreetFighter"
print(thisdict)
