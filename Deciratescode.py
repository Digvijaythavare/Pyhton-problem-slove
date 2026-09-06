def greet(func):
    name = input("Enter your name: ")
    def respect():
        print("Welcome to the programming world, " + name)
        func()
        print("Thank you for using this program, ")
    return respect

@greet
def hello():
    print("Good morning! friends. ")
hello()    