# Lambda, map, filter, reduce
# lambdas are often used with functions like map filter reduce
# lambda arguments : expression

nums = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, nums))
print(squared)  # Output: [1, 4, 9, 16]