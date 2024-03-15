def func1(func2):
    func2()
    print("The function executed now end the program..")


@func1
def func2():
    print("Enter function 2, decorator activated")
