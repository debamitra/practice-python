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



names = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 42, 91, 67]

# Q1. Print each name along with their score using zip()

comb = zip(names,scores)
for c in comb:
    print(c)

# Q2. Print the index + name + score using enumerate() and zip()

en = enumerate(zip(names,scores))
for e in en:
    print(e)


# Q3. Use filter() to get names of students who passed (score >= 60)
filtered = list(filter(lambda x : x[1] > 60 , zip(names,scores) ))  
print(filtered)

# Q4. Use map() to create a new list of grades:
#      "Pass" if score >= 60, else "Fail"



# Q5. Check if all students passed using all()

# Q6. Check if at least one student failed using any()



# zip(*iterables)

# Explanation:
#	•	Takes multiple iterables (like lists, tuples).
#	•	Returns an iterator of tuples — pairing up elements by index.
#	•	Stops when the shortest iterable is exhausted.
# Example - zip(["a", "b"], [1, 2])  # → [("a", 1), ("b", 2)]

# enumerate(iterable, start=0)

# Explanation:
#	•	Adds an index counter to an iterable.
#	•	Returns an iterator of tuples → (index, item)
# Example - enumerate(["a", "b"], start=1)  # → [(1, "a"), (2, "b")]

# filter(function, iterable)

# Explanation:
# Returns an iterator with only items where function(item) is True.
# Can be converted to a list using list().
# Example - filter(lambda x : x>0, [-2,3,0]) # → [3]

# map(function,iterable)

# Explanation:
# Applies the function to every item of the iterable.
# Returns an iterator. Use list() to view results.
# Example - map(lambda x: x*2, [1,2,3] )   # → [2, 4, 6]

# all(iteratble)
# all([True, True, False])  # → False
# any(iterable)
# any([0, None, "hello"])  # → True







