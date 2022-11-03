"Decorators with additional parameter in func(parameter)"
def decorator(func):
    def wrapper(wrapper_parameter): # an parameter must be addet wo wrapper in func has got an parameter
        print("Decoration begins")
        func(wrapper_parameter)
        print("Decorations ends")
    return wrapper

"For, unlimited kind of cufunctions and parameters"
def decorator_2(func):
    def wrapper(*args,**kwargs): # args for list and kwargs for dictionary
        print("Decoration begins")
        func(*args,**kwargs)
        print("Decorations ends")
    return wrapper
    
@decorator
def func(func_parameter):
    print(func_parameter)

func("Hello")