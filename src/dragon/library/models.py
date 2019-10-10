import datetime

from django.db import models
from django.db.models import Model, CharField, TextField, AutoField, IntegerField, ManyToManyField
from django.shortcuts import get_object_or_404

# These classes are mapped to database entries,
# but can also be instantiated in python code.
# They can be retrieved from the database via queries
# Note that if the query fails an exception is thrown
# the shortcut `get_object_or_404` catches this exception
# and returns a 404 response as it was not found, this
# is a strongly recommended way of accessing objects


def return_date():
    """the default due date is 2 weeks from borrow"""
    now = datetime.date.today()
    return now + datetime.timedelta(days=14)


class Genre(models.Model):
    name = CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


# todo: semantically it makes sense for the library items to be mostly static data
# todo: so any fields that are likely to change temporarily (such as being borrowed)
# todo: should be moved into a separate model that reflects a more dynamic aspect of
# todo: the library system.


class Item(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=200)
    description = TextField(max_length=1000, blank=True, default='')
    notes = TextField(max_length=1000, blank=True, default='')
    tags = ManyToManyField(Tag, blank=True)
    genres = ManyToManyField(Genre, blank=True)

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

    def is_available(self):
        query = Borrow.objects.filter(item_id=self.id)
        return len(query) == 0

    def get_due_date(self):
        borrow = Borrow.objects.get(item=self.id)
        return borrow.due_date

    # borrow currently doesn't use the user, but this will make the item unavailable
    def borrow_item(self):
        now = datetime.date.today()
        borrow_date = now
        due_date = now + datetime.timedelta(days=14)
        lone = Borrow(item_id=self.id, borrow_date=borrow_date, due_date=due_date)
        lone.save()

    def return_item(self):
        loan = get_object_or_404(Borrow, item_id=self.id)
        loan.delete()


class Book(Item):
    isbn = CharField(max_length=16, blank=True, default='')
    edition = IntegerField(blank=True, default=1)
    year = IntegerField(blank=True, default=2000)

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

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 1


class Card(Item):
    deck_type = CharField(max_length=16, blank=True, default='')
    minplayers = IntegerField(blank=True, default=1)
    maxplayers = IntegerField(blank=True, default=8)
    mingamelength = IntegerField(blank=True, default=0)
    maxgamelength = IntegerField(blank=True, default=10)

    difficulty_choices = ((0, 'Easy'), (1, 'Medium'), (2, 'Hard'))
    difficulty = IntegerField(choices=difficulty_choices, default=0)

    # due_date = DateField(default=return_date)

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 2


class Borrow(Model):
    """
    Borrows are used to track when something is out of the library
    When something is taken out an entry in this table is added
    When it is returned this table is modified to indicate so
    Currently that involves deleting the entry
    todo: archive borrows
    """
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now=True)
    due_date = models.DateField(auto_now_add=True)

# notes (Kieran): I would prefer having default text being an empty string
#                 This would be simpler to test for and give custom output
#                 such as "no description" and take less data. Can we make
#                 this consistent?
