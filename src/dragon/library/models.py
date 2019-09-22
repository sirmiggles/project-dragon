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


class Book(Item):
    isbn = CharField(max_length=16, blank=True, default='N/A')

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
