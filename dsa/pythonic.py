# lambdas
# lambda args : expression
# Write a lambda to find the square of a number.
# Use a lambda with filter() to extract odd numbers from a list.
# Use a lambda with map() to convert a list of strings to uppercase.

square = lambda x : x * x
print(square(5))
numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
even_nos_iter = filter(lambda x : x % 2 == 1, numbers)
print(list(even_nos_iter))
mystrings = ["hello", "world", "mine","ordain"]
uppers = map(lambda x : x.upper(), mystrings)
print(list(uppers))



# list cmprehensions
# expression for item in iterable  if condition
