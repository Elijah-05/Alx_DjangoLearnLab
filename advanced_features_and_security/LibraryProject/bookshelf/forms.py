from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
    
    def clean_publication_year(self):
        year = self.cleaned_data['publication_year']
        if year < 0:
            raise forms.ValidationError("Year cannot be negative.")
        return year
