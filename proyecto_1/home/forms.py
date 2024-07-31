
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
        labels = {
            'title': 'Título',
            'author': 'Autor',
            'published_date': 'Fecha de Publicación',
        }