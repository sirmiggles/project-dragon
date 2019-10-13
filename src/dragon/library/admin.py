from django.contrib import admin

# These models will be added to the Django admin page
from .models import Book, Game, Tag

# In order to access the models, they need to be registered to
# the admin site
admin.site.register(Book)
admin.site.register(Game)
admin.site.register(Tag)
