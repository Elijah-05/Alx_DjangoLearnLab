from rest_framework import serializers
from django.utils import timezone
from .models import Author, Book

"""
Serializers convert model instances into JSON for API responses.
They also validate incoming data before creating/updating objects.
"""


class BookSerializer(serializers.ModelSerializer):
    """
    Serializes all fields of the Book model.
    Includes custom validation to prevent future publication years.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom field-level validation example
    def validate_publication_year(self, value):
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes the Author model and includes nested
    BookSerializer data for related books.

    `books` is read-only to prevent creating books inside
    an author POST endpoint. It uses the related_name on Book.author.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
