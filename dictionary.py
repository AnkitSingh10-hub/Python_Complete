# A dictionary is a key value pair which is ordered(indexed), changeable(mutable) and do not allow duplicates.
thisdict = {"brand": "Ford", "model": "Mustang", "Year": 1964}
print(thisdict)

for i in thisdict.values():
    print(i)

if "brand" in thisdict.keys():
    print(True)

if "Ford" in thisdict.values():
    print(True)

print(thisdict.items())