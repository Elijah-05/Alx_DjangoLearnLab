from django.db import models

# Create your models here.

"""
The Author and Book models define a one-to-many relationship.
- One Author can have multiple Books.
- Book includes a ForeignKey to Author.
"""

class Author(models.Model):
    # Stores the author's full name
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents published books.
    Each book is associated with exactly one author through a ForeignKey.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()

    # Establishes Author → Books relationship
    author = models.ForeignKey(
        Author,
        related_name='books',   # This allows reverse access via author.books
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
