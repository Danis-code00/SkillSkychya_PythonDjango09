# This is a function for taking name and returns greating
# def helloWorld(name):
#     return f"Hello, {name}"

# print(helloWorld("Human"))
def Calculator():
    num1, num2 = map(int, input("Enter two numbers : ").split())
    print(f"Addition: {num1 + num2}")


Calculator();
