# decorators are functions that wrap other function to modify or extend its behavior
# def decorator(func):
#     def wrapper():
#         print("before function call")
#         func()
#         print("after function call")
#     return wrapper

# @decorator
# def greet():
#     print("hello")

# greet()


# great for logging timing caching

# 1.	Create a decorator that prints “Start” and “End” around a function.

def decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@decorator
def greet():
    print("Hello")

greet()

# 2.	Create a decorator that measures the time a function takes to run.

import time


def time_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("time taken to run this funtion: ")
        print(end - start)
    return wrapper

@time_decorator
def sample():
    print("sample")
    time.sleep(2)

sample()



