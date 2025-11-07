from .models import Book, Library

library_name = "Central Library"

# Query books filtered by author
books = Book.objects.filter(author='Jane Austen')

# Retrieving all books by library
library = Library.objects.get(name=library_name)
all_library_books = library.books.all()

# Retrieve a Librarian
library = Library.objects.get(name=library_name)
librarian = library.librarian