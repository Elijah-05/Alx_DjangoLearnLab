from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# Create your views here.

"""
This file defines the views for handling CRUD operations for Book objects
using Django REST Framework's generic class-based views.

These views automatically provide common behavior such as:
- Retrieving lists of objects
- Fetching objects by ID
- Creating, updating, deleting objects

We also apply permission classes to protect write operations.
"""


# ---------------------------
# LIST ALL BOOKS (READ-ONLY)
# ---------------------------
class BookListView(generics.ListAPIView):
    """
    Retrieves all Book instances.
    No authentication required (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ----------------------------
# GET A SINGLE BOOK BY ID
# ----------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single Book instance by its primary key (ID).
    No authentication required (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ----------------------------
# CREATE A NEW BOOK
# ----------------------------
class BookCreateView(generics.CreateAPIView):
    """
    Creates a new Book instance.
    Only authenticated users can create books.

    Custom behavior:
    - Ensures serializer validations run correctly.
    - Could be extended to auto-assign fields based on request.user.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ----------------------------
# UPDATE AN EXISTING BOOK
# ----------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    Updates a book instance.
    Only authenticated users can update books.

    Custom behavior:
    - Override perform_update() if extra logic is needed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Example custom logic
        print("User updated book:", self.request.user)
        serializer.save()



# ----------------------------
# DELETE A BOOK
# ----------------------------
class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a book instance.
    Only authenticated users can delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
