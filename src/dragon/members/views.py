from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import User, ClubMember


def members(request):
    clubmembers = ClubMember.objects.order_by('FirstName')
    return render(request, 'members/members.html', {'clubmembers': clubmembers})


def user_form(request):
    return render(request, 'members/user_form.html')


def add_user(request):
    username = request.POST['username']
    if username != '':
        user = User(username=username)
        user.save()
    return HttpResponseRedirect('/members/')


def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'members/user_detail.html', {'user': user})


def remove_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return HttpResponseRedirect('/members/')