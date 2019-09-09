from django.db import models


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=True, default='')
    notes = models.CharField(max_length=1000, blank=True, default='')
    available = models.BooleanField(default=True)


class Book(Item):
    isbn = models.CharField(max_length=16, blank=True, default='')

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, name):
        book = cls(name=name)
        return book


class Game(Item):
    players = models.IntegerField(blank=True, default=1)

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, name):
        game = cls(name=name)
        return game