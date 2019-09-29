import datetime

from django.db.models import Model, CharField, TextField, AutoField, BooleanField, IntegerField, ManyToManyField, \
    DateField


class Tag(Model):
    name = CharField(max_length=200)

    def __str__(self):
        return self.name


def return_date():
    now = datetime.date.today()
    return now + datetime.timedelta(days=14)


class Item(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=200)
    description = TextField(max_length=1000, blank=True, default='')
    notes = TextField(max_length=1000, blank=True, default='')
    available = BooleanField(default=True)
    tags = ManyToManyField(Tag)
    due_date = DateField(default=return_date)

    type_choices = ((0, 'Book'), (1, 'Game'), (2, 'Card'))
    type = IntegerField(choices=type_choices)

    condition_choices = (
        (0, 'Excellent'),
        (1, 'Very good'),
        (2, 'Good'),
        (3, 'Fair'),
        (4, 'Bad')
    )
    condition = IntegerField(choices=condition_choices)


class Book(Item):
    isbn = CharField(max_length=16, blank=True, default='N/A')
    edition = IntegerField(blank=True, default = 1)
    year = IntegerField(blank=True, default = 2000)
    
    genre_choices = (
        (0, 'Fantasy'), 
        (1, 'Romance'), 
        (2, 'Sci-Fi'), 
        (3, 'Western'), 
        (4, 'Thriller'), 
        (5, 'Mystery'), 
        (6, 'Detective'), 
        (7, 'Dystopia'),
        (8, 'Other')
    )
    genre = IntegerField(choices=genre_choices, default=8)

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 0


class Game(Item):
    minplayers = IntegerField(blank=True, default=1)
    maxplayers = IntegerField(blank=True, default=8)
    mingamelength = IntegerField(blank=True, default=0)
    maxgamelength = IntegerField(blank=True, default=10)
    
    difficulty_choices = ((0, 'Easy'), (1, 'Medium'), (2, 'Hard'))
    difficulty = IntegerField(choices=difficulty_choices, default=0)

    genre_choices = (
        (0, 'Wargames'), 
        (1, 'Roll & Move games'), 
        (2, 'Worker Placement games'), 
        (3, 'Cooperative games'), 
        (4, 'Area Control games'), 
        (5, 'Secret Identity games'), 
        (6, 'Legacy games'), 
        (7, 'Combat games'), 
        (8, 'Party games'), 
        (9, 'Other')
    )
    genre = IntegerField(choices=genre_choices, default=0)

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 1


class Card(Item):
    deck_type = CharField(max_length=16, blank=True, default='N/A')
    # due_date = DateField(default=return_date)

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 2
