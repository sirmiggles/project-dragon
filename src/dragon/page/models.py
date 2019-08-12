from django.db import models


# Create your models here.

class Item(models.Model):
    id = models.ForeignKey
    title = models.CharField(max_length=200)
    published_date = models.DateField
    type = models.CharField(max_length=200)
    remarks = models.CharField(max_length=200)
