"Decoration is wrapping funcitions in another function"
def func():
    print("Function")

def wrapper(func):
    print("Hello")
    func()
    print("Goodbye")

def function_generaotr():
    def new_function():
        print("New function")
    return new_function

new_func = function_generaotr()
new_func()
wrapper(func)