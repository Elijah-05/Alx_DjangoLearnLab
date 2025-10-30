# Retrieve all Book instances
from .models import Book

books = Book.objects.all()
print(books)

# Expected Output:
# <QuerySet [<Book: 1984 by George Orwell (1949)>]>
