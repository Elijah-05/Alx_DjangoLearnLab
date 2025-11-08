from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from .models import Library, Book

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def library_detail(request, pk):
    library = get_object_or_404(Library.objects.prefetch_related('books__author'), pk=pk)
    return render(request, 'relationship_app/library_detail.html', {'library': library})

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
    
class LoginView(CreateView):
    template_name = 'relationship_app/login.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('book_list')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"