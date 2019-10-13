from django.views.generic import ListView
from django.db.models import Q
from .models import Borrow


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
        return context


class BorrowedList(ListView):
    model = Borrow
    template_name = "library/borrowed.html"
    context_object_name = ""
