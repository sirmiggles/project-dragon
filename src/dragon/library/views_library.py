from django.views.generic import ListView
from django.db.models import Q
from .models import Borrow, Tag, Genre, Item, Book, Card, Game, Series
from django.contrib.auth.decorators import login_required, user_passes_test


def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""

    def in_groups(user):
        if user.is_authenticated:
            if bool(user.groups.filter(name__in=group_names)) | user.is_superuser:
                return True
        return False

    return user_passes_test(in_groups)


class ItemList(ListView):

    # template_name = "library/item/all.html"

    def get_queryset(self):
        query = self.request.GET.get("search")
        order = self.request.GET.get("order")
        result = self.model.objects.all
        if order is not None:
            result = self.model.objects.order_by(order)
        else:
            result = self.model.objects.order_by("name")
        if query is not None:
            lookup = Q(name__icontains=query) | Q(tags__name__icontains=query) | Q(genres__name__icontains=query)
            lookup = lookup | Q(series__name__icontains=query)

            if self.model == Book:
                lookup = lookup | Q(isbn__icontains=query) | Q(year__icontains=query)
            elif self.model == Card:
                lookup = lookup | Q(deck_type__icontains=query)

            return result.filter(lookup)
        else:
            return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["searchterm"] = self.request.GET.get("search", "")
        context["order"] = self.request.GET.get("order", "")
        context["tags"] = Tag.objects.all()
        context["genres"] = Genre.objects.all()
        context["series"] = Series.objects.all()
        return context


class BorrowedList(ListView):
    model = Borrow
    template_name = "library/borrowed.html"
    context_object_name = ""
