class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    
    def __repr__(self):
        return f"Book: {self.title} {self.author}"

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __len__(self):
        return len(self.title)
    

b1 = Book("Python 101", "Deb")
b2 = Book("Python 101", "Deb")
print(b1 == b2)      # True
print(len(b1))       # 10
print(str(b1))       # Python 101 by Deb
print(repr(b1)) 

