from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200)


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=True, default='')
    notes = models.CharField(max_length=1000, blank=True, default='')
    available = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag)


class Book(Item):
    isbn = models.CharField(max_length=16, blank=True, default='')

    def __str__(self):
        return self.name


class Game(Item):
    players = models.IntegerField(blank=True, default=1)

    def __str__(self):
        return self.name
