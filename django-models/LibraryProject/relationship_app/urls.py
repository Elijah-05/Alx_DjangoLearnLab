from django.urls import path
from .views import list_books

urlpatterns = [
    path('books/', list_books, name='book_list'),  # Function-based view
    path('library/<int:pk>/', list_books.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
]
