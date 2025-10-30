# Retrieve all Book instances
from .models import Book

books = Book.objects.get()
print(books)

# Expected Output:
# <QuerySet [<Book: 1984 by George Orwell (1949)>]>
