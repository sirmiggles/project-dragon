from django.views.generic import ListView
from django.db.models import Q
from .models import Borrow, Tag, Genre
from django.contrib.auth.decorators import login_required, user_passes_test


def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""

    def in_groups(user):
        if user.is_authenticated:
            if bool(user.groups.filter(name__in=group_names)) | user.is_superuser:
                return True
        return False

    return user_passes_test(in_groups)


# this isn't been used, @dan switched it back, so I (@kieran) can experiment
class ItemList(ListView):

    # template_name = "library/item/all.html"

    def get_queryset(self):
        query = self.request.GET.get("search")
        if query is not None:
            return self.model.objects.filter(Q(name__icontains=query))
        else:
            return self.model.objects.order_by("name")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["searchterm"] = self.request.GET.get("search", "")
        context["tags"] = Tag.objects.all()
        context["genres"] = Genre.objects.all()
        return context


class BorrowedList(ListView):
    model = Borrow
    template_name = "library/borrowed.html"
    context_object_name = ""
