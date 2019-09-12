from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import User


def members(request):
    users = User.objects.order_by('username')
    return render(request, 'members/members.html', {'users': users})


def user_form(request):
    return render(request, 'members/user_form.html')


def add_user(request):
    username = request.POST['username']
    if username != '':
        user = User(username=username)
        user.save()
    return HttpResponseRedirect('/members/')