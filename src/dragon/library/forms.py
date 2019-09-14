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
        labels = {
            'name': 'Name',
            'description': 'Description',
            'notes': 'Notes',
            'isbn': 'ISBN',
            'condition': 'Condition'
        }


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
        labels = {
            'name': 'Name',
            'description': 'Description',
            'notes': 'Notes',
            'minplayers': 'Min. Players',
            'maxplayers': 'Max. Players',
            'condition': 'Condition'
        }
