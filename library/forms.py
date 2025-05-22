from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        module = Book
        fields = ['title', 'author', 'published_date', 'isbn', 'pages']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }