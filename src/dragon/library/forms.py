from django import forms
from .models import Book, Game, Card, Tag, Genre, Series

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
            'condition',
            'genres',
            'tags'
        ]
        labels = {
            'name': 'Name',
            'description': 'Description',
            'notes': 'Notes',
            'isbn': 'ISBN',
            'edition': 'Edition',
            'year': 'Year',
            'condition': 'Condition',
            'genres': 'Genres',
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
            'condition',
            'genres',
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
            'condition': 'Condition',
            'genres': 'Genres',
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
            'condition',
            'deck_type',
            'genres',
            'tags'
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
            'deck_type': 'Deck Type',
            'genres': 'Genres',
            'tags': 'Tags'
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = [
            'name'
        ]
        labels = {
            'name': 'Tag Name'
        }


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = [
            'name'
        ]
        labels = {
            'name': 'Genre Name'
        }


class SeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = [
            'name'
        ]
        labels = {
            'name': 'Series Name'
        }
