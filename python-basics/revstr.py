'''
Beginner: Reverse a String
Skill: String manipulation.
Problem: Write a function that takes a string as input and returns the string reversed.
Example Input: "hello"
Example Output: "olleh"
'''
#Indexing
#[index]
#Slicing
#[start:stop:step]

text = "Python Programming"

last = text[-1]
print(last)

last_two = text[-4::2]
print(last_two)

reverse = text[::-1]
print(reverse)

text1 = "hello world"
print(text1.title())
print(text1.capitalize())

text = "Hello, World!"

# join() is a string method called on a separator string
# Syntax: separator.join(iterable)
no_punctuation = ''.join(char for char in text if char.isalnum())
print(no_punctuation)

