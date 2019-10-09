from django.views.generic import ListView
from .models import Item, Borrow


class ItemList(ListView):
    model = Item
    template_name = "library/item/all.html"
    context_object_name = "items"
    # todo add ordering


class BorrowedList(ListView):
    model = Borrow
    template_name = "library/borrowed.html"
    context_object_name = ""
