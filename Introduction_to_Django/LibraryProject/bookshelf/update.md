# Update the title of the created book
from .models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

print(book)

# Expected Output:
# <Book: Nineteen Eighty-Four by George Orwell (1949)>
