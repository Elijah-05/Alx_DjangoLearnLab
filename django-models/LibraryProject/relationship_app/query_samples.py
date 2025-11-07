from .models import Book, Library

# Query books filtered by author
books = Book.objects.filter(author='Jane Austen')

# Retrieving all books by library
library = Library.objects.get(name='Central Library')
all_library_books = library.books.all()

# Retrieve a Librarian
library = Library.objects.get(name="Central Library")
librarian = library.librarian