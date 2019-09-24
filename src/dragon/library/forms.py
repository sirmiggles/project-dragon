from django import forms
from .models import Book, Game, Card


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'description',
            'notes',
            'isbn',
            'edition',
            'year',
            'genre',
            'condition'
        ]
        labels = {
            'name': 'Name',
            'description': 'Description',
            'notes': 'Notes',
            'isbn': 'ISBN',
            'edition': 'Edition',
            'year': 'Year',
            'genre': 'Genre',
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
            'mingamelength',
            'maxgamelength',
            'difficulty',
            'genre',
            'condition'
        ]
        labels = {
            'name': 'Name',
            'description': 'Description',
            'notes': 'Notes',
            'minplayers': 'Min. Players',
            'maxplayers': 'Max. Players',
            'mingamelength': 'Min. Game Length (minutes)',
            'maxgamelength': 'Max. Game Length (minutes)',
            'difficulty': 'Difficulty',
            'genre': 'Genre',
            'condition': 'Condition'
        }

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = [
            'name',
            'description',
            'notes',
            'condition',
            'deck_type'
        ]
        labels = {
            'name': 'Name',
            'description': 'Description',
            'notes': 'Extra Notes',
            'condition': 'Condition',
            'deck_type': 'Deck Type'
        }