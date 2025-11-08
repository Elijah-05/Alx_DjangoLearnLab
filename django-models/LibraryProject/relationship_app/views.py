from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Library, Book

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# class based view

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


    def get_context_data(self, **kwargs):
        """Injects additional context data specific to the library."""
        context = super().get_context_data(**kwargs)  # Get default context data
        library = self.get_object()  # Retrieve the current library instance
        context['books'] = library.books.all()  # Add all books in the library to the context
        return context