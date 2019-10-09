from django import forms
from .models import Book, Game, Card

# These classes produce a standard format to create a form
# they can be instantiated in `views.py` and added to the
# context of the render function to create the html form


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
            'condition',
            'tags'
        ]
        labels = {
            'name': 'Name',
            'description': 'Description',
            'notes': 'Notes',
            'isbn': 'ISBN',
            'edition': 'Edition',
            'year': 'Year',
            'genre': 'Genre',
            'condition': 'Condition',
            'tags': 'Tags'
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
            'condition',
            'tags'
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
            'condition': 'Condition',
            'tags': 'Tags'
        }


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
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
            'condition',
            'deck_type'
        ]
        labels = {
            'name': 'Name',
            'description': 'Description',
            'notes': 'Extra Notes',
            'minplayers': 'Min. Players',
            'maxplayers': 'Max. Players',
            'mingamelength': 'Min. Game Length (minutes)',
            'maxgamelength': 'Max. Game Length (minutes)',
            'difficulty': 'Difficulty',
            'condition': 'Condition',
            'deck_type': 'Deck Type'
        }