class Book:

    book_types = ('Hardcover', 'Paperbook')

    def __init__(self,name,book_types,weight):
        self.name = name
        self.book_types = book_types
        self.weight = weight

    @classmethod
    def hardcover(cls,name,weight):
        return Book(name, Book.book_types[0], weight)
    
    @classmethod
    def paperbook(cls, name, weight):
        return Book(name, Book.book_types[1], weight)
    
    def __str__(self):
        return f"Book name is {self.name} and weight is {self.weight}"

print(Book.hardcover("ABC", 1000))
print(Book.paperbook("ABC", 1000))
