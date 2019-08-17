from django.db import models


# Create your models here.

class Item(models.Model):
    id = models.ForeignKey
    remarks = models.CharField(max_length=200)

    @property
    def is_a_book(self):
        return False

class Published(Item):
    published_date = models.DateField
    publisher = models.CharField(max_length=200)


class Book(Published):
    isbn = models.IntegerField()
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    @property
    def is_a_book(self):
        return True
