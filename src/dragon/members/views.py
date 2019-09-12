from django.shortcuts import render

from .models import User


def members(request):
    users = User.objects.order_by('username')
    return render(request, 'members/members.html', {'members': users})
