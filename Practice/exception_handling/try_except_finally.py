
try:
    b = 10
    c = 0
    a = b/c
    print(a)

except ZeroDivisionError as e:
    print(e)
except NameError:
    print("This is a name error")
else:
    print("Everything worked completely fine")
finally:
    print("This is the final statement")