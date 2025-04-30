# Example:

def make_multiplier(x):
    def mul_by_n(n):
        return x*n
    return mul_by_n

times3 = make_multiplier(3)
print(times3(10))  # Output: 30


def logger(func):
    def wrapper_func(*args, **kwargs):
        print("Function is being called")
        func(*args, **kwargs)
    return wrapper_func


@logger
def greet():
    print("Hi!")

# Should output:
# Function is being called
# Hi!
greet()


# Decorator that logs the name of the function being called + arguments passed
# Calling add with args: (2, 3), kwargs: {}


def logger(func):
    def wrapper_func(*args,**kwargs):
        print(f"Calling add with args: {args}, kwargs: {kwargs}")
        
        return func(*args,**kwargs)
    return wrapper_func



@logger
def add(x, y):
    return x + y

print(add(2, 3))



from functools import wraps


def logger(func):
    @wraps
    def wrapper_func(*args,**kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        return func(*args,**kwargs)
    return wrapper_func