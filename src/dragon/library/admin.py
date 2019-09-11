from django.contrib import admin

# Register your models here.

from .models import Book, Game, Tag

admin.site.register(Book)
admin.site.register(Game)
admin.site.register(Tag)

