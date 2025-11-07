from .models import Author, Book, Library, Librarian

library_name = "Central Library"
author_name = "Jane Austen"

# Query books filtered by author
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)

# Retrieving all books by library
library = Library.objects.get(name=library_name)
all_library_books = library.books.all()

# Retrieve a Librarian
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)