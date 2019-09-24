from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import User, ClubMember


def members(request):
    clubmembers = ClubMember.objects.order_by('firstName')
    return render(request, 'members/members.html', {'clubmembers': clubmembers})


def user_form(request):
    return render(request, 'members/user_form.html')


def add_clubmember(request):
    firstname = request.POST['firstName']
    surname = request.POST['surname']
    if firstname != '':
        clubmember = ClubMember(firstName=firstname, surname=surname)
        clubmember.save()
    return HttpResponseRedirect('/members/')


def clubmember_detail(request, clubmember_id):
    clubmember = get_object_or_404(ClubMember, pk=clubmember_id)
    return render(request, 'members/user_detail.html', {'clubmember': clubmember})


def remove_clubmember(request, clubmember_id):
    clubmember = get_object_or_404(ClubMember, pk=clubmember_id)
    clubmember.delete()
    return HttpResponseRedirect('/members/')
