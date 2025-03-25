# Given:
numbers = [4, 9, 1, 7, 12]

# Q1. Find the length of the list using a built-in function
# Q2. Find the maximum and minimum numbers
# Q3. Calculate the sum of all the numbers
# Q4. Get the average using sum() and len()
# Q5. Sort the list in descending order using sorted()
# sorted(iterable, key=key, reverse=reverse)
# parameter          desc
# ------------------------
# iterable           Required. The sequence to sort, list, dictionary, tuple etc.
# key                Optional. A Function to execute to decide the order. Default is None
# reverse            Optional. A Boolean. False will sort ascending, True will sort descending. Default is False

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers)/len(numbers))
print(sorted(numbers, reverse=True ))