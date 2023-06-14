a = 100
if a > 100:
    print(False)

else:
    print(True)


b = None
if b is False:
    print("It is False")
elif b is True:
    print("It is True")
elif b is None:
    print("It is empty")
elif b is not None:
    print("a has some item, it is not none")
