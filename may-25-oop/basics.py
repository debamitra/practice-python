class Dog:
    # Special method that runs when i create an object
    # self refers to current object
    def __init__(self,name):
        self.name = name

    def bark(self):
        return f"{self.name} says Woof"

dog1 = Dog("Scooby")
print(dog1.bark())


	# •	__init__(self, title, author)
	# •	summary() method that prints "Title by Author"

    # book = Book("Python 101", "Deb")
    # book.summary()  # Output: Python 101 by Deb
    # Add a method is_long() that returns True if a book title has more than 10 characters.

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    
    def summary(self):
        return f"Output: {self.title} by {self.author}"
    
    def is_long(self):
        return len(self.title) > 10
            

book = Book("Python 101", "Deb")
print(book.summary() ) # Output: Python 101 by Deb
print(book.isLong())
