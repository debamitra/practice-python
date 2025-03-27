# decorators are functions that wrap other function to modify or extend its behavior
def decorator(func):
    def wrapper():
        print("before function call")
        func()
        print("after function call")
    return wrapper

@decorator
def greet():
    print("hello")

greet()