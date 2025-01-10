# iterators practice

# 1. Create a list of numbers from 1 to 10
# 2. Create an iterator that yields the numbers from 1 to 10
# 3. Create a generator that yields the numbers from 1 to 10
# 4. Create a list of numbers from 1 to 10 using a generator expression
# 5. Create a list of numbers from 1 to 10 using a generator expression
# 6. Create a list of numbers from 1 to 10 using a generator expression
# 7. Create a list of numbers from 1 to 10 using a generator expression
# 8. Create a list of numbers from 1 to 10 using a generator expression
# 9. Create a list of numbers from 1 to 10 using a generator expression
# 10. Create a list of numbers from 1 to 10 using a generator expression

list_of_numbers = [x for x in range(1,11)]
print(list_of_numbers)

# what are iterables? lists, tuples, strings, sets, dictionaries, generators, etc
# any python object that can be used in a for loop
# can be used with the iter() function to get an iterator
print(iter(list_of_numbers))

