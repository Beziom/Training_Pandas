import time 
"Decorators - how doest them woorkd in func() without parameter"
def decorator(func):
    def wrapper():
        print("Decoration begins")
        func()
        print("Decorations ends")
    return wrapper

def duration_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        duration = time.time() - start_time
        print(f"Duration {duration}s")
    return wrapper

def double_decorator(func):
    def wrapper():
        func()
        func()
    return wrapper

@double_decorator   
@duration_decorator # We we using decorator which we would like to use
@decorator
def func():
    print("Function")
    time.sleep(1)


func()



