# Aggregation Example

# Book Class
class Book:
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f"Book({self.title})"

# Library Class (Aggregation)
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise ValueError("Only Book instances can be added")
        self.books.append(book)

    def __repr__(self):
        return f"Library({self.books})"

# Usage
book1 = Book("1984")
book2 = Book("Brave New World")
library = Library()
library.add_book(book1)
library.add_book(book2)
print(library)  # Output: Library([Book(1984), Book(Brave New World)])
