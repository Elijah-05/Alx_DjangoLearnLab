from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics
from rest_framework import generics, permissions, filters
from django_filters import rest_framework
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
    permission_classes = [IsAuthenticatedOrReadOnly]

    """
    Retrieves all Book instances with support for:
    - Filtering by title, publication_year, and author
    - Searching by title and author's name
    - Ordering by any field, especially title and publication_year

    Examples:
    Filtering:
        /api/books/?title=Dune
        /api/books/?publication_year=1965
        /api/books/?author=1

    Searching:
        /api/books/?search=dune

    Ordering:
        /api/books/?ordering=title
        /api/books/?ordering=-publication_year
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Enable filtering, searching, ordering
    filter_backends = [
        rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    # Fields available for filtering
    filterset_fields = ['title', 'publication_year', 'author']

    # Fields searchable by users
    # Note: searching across FK uses the syntax: author__name
    search_fields = ['title', 'author__name']

    # Fields users are allowed to order by
    ordering_fields = ['title', 'publication_year', 'author']

    # Default ordering (optional)
    ordering = ['title']


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
    permission_classes = [IsAuthenticatedOrReadOnly]


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
    permission_classes = [IsAuthenticated]


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
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]
