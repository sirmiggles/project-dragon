from django.db.models import Model, CharField, AutoField, BooleanField, IntegerField, ManyToManyField


class Tag(Model):
    name = CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=200)
    description = CharField(max_length=1000, blank=True, default='')
    notes = CharField(max_length=1000, blank=True, default='')
    available = BooleanField(default=True)
    tags = ManyToManyField(Tag)

    type_choices = ((0, 'book'), (1, 'game'))
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
    isbn = CharField(max_length=16, blank=True, default='')

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 0


class Game(Item):
    players = IntegerField(blank=True, default=1)

    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 1
