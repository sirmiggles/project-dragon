import datetime

from django.db import models
from django.db.models import Model, CharField, TextField, AutoField, BooleanField, IntegerField, ManyToManyField, \
    DateField

from ..members.models import User


# These classes are mapped to database entries,
# but can also be instantiated in python code.
# They can be retrieved from the database via queries
# Note that if the query fails an exception is thrown
# the shortcut `get_object_or_404` catches this exception
# and returns a 404 response as it was not found, this
# is a strongly recommended way of accessing objects


class Tag(Model):
    name = CharField(max_length=200)

    def __str__(self):
        return self.name


def return_date():
    """the default due date is 2 weeks from borrow"""
    now = datetime.date.today()
    return now + datetime.timedelta(days=14)


# todo: semantically it makes sense for the library items to be mostly static data
# todo: so any fields that are likely to change temporarily (such as being borrowed)
# todo: should be moved into a separate model that reflects a more dynamic aspect of
# todo: the library system.


class Item(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=200)
    description = TextField(max_length=1000, blank=True, default='')
    notes = TextField(max_length=1000, blank=True, default='')
    # todo: this should be an inferred property from a borrowed item table
    available = BooleanField(default=True)
    tags = ManyToManyField(Tag)
    # todo: refactor this into borrowed item table
    # ??? (Kieran) I believe this will set the default due date for all items as 2 weeks from
    # ???          when the database applies this migration, which doesn't make any sense to me
    due_date = DateField(default=return_date)
    # our database model is a discriminated union, these are the options of the discriminate
    type_choices = ((0, 'book'), (1, 'game'), (2, 'card'))
    type = IntegerField(choices=type_choices)

    condition_choices = (
        (0, 'excellent'),
        (1, 'very good'),
        (2, 'good'),
        (3, 'fair'),
        (4, 'bad')
    )
    condition = IntegerField(choices=condition_choices)

    def is_available(self):
        return self.available

    def get_due_date(self):
        return self.due_date

    # req: borrow table to be updated via this method
    def borrow(self, user):
        pass


class Book(Item):
    isbn = CharField(max_length=16, blank=True, default='')
    edition = IntegerField(blank=True, default=1)
    year = IntegerField(blank=True, default=2000)

    # todo: make genre list editable rather than hard coded.
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
    deck_type = CharField(max_length=16, blank=True, default='')

    # due_date = DateField(default=return_date)

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 2


class Borrow(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    due_date = models.DateField(auto_now_add=True)

# notes (Kieran): I would prefer having default text being an empty string
#                 This would be simpler to test for and give custom output
#                 such as "no description" and take less data. Can we make
#                 this consistent?
