class Book:
    def __init__(self,title,author,year):
        self.title =title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"( Book: {self.title} , {self.author} , {self.year})"

    def __eq__(self,other):
        return self.title == other.title and self.author == other.author and self.year == other.year
    
    def __str__(self):
        return f"Book : {self.title} by {self.author} written in {self.year}"
    

class Library:
    
