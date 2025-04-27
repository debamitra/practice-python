# Topic 1: Functions as First-Class Objects in Python

# you can assign them to variables
# pass them as arguments
# return them from other functions
# store them in lists, dicts 

#patterns - higher order funtions, decorators and callbacks


def greet(name):
    return f"Hello: {name}!"

sayhello = greet
print(sayhello("deba"))



# Example

def apply_twice(func, multiplier):
    return func(func(multiplier))
def double(n): return n * 2
print(apply_twice(double, 5))  # Output: 20


def choose_operation(op):
    # def add(n):
    #     return n + 10
    # def mul(n):
    #     return n * 10
    # if op =="add":
    #     return add
    # if op == "mul":
    #     return mul
    operations = {
        "add": lambda x:x+10,
        "mul": lambda x:x*10
    }
    return operations.get(op)

add_func = choose_operation("add")
print(add_func(3))  # Output: 13
mul_func = choose_operation("mul")
print(mul_func(3))  # Output: 30
