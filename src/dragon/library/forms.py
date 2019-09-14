from django import forms
from .models import Book, Game


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'description',
            'notes',
            'isbn',
            'condition'
        ]


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            'name',
            'description',
            'notes',
            'minplayers',
            'maxplayers',
            'condition'
        ]