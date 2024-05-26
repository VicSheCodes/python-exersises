# Composition Example

# Book Class
class Book:
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f"Book({self.title})"

# Library Class (Composition)
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        book = Book(title)
        self.books.append(book)

    def __repr__(self):
        return f"Library({self.books})"

# Usage
library = Library()
library.add_book("1984")
library.add_book("Brave New World")
print(library)  # Output: Library([Book(1984), Book(Brave New World)])

