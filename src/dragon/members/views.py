from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import User, ClubMember
from .forms import ClubMemberForm


def members(request):
    clubmembers = ClubMember.objects.order_by('firstName')
    return render(request, 'members/members.html', {'clubmembers': clubmembers})


def clubmember_form(request):
    form = ClubMemberForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, "members/clubmember_form.html", {'form': form})


def add_clubmember(request):
    firstname = request.POST['firstName']
    surname = request.POST['surname']
    if firstname != '':
        clubmember = ClubMember(firstName=firstname, surname=surname)
        clubmember.save()
    return HttpResponseRedirect('/members/')


def clubmember_detail(request, clubmember_id):
    clubmember = get_object_or_404(ClubMember, pk=clubmember_id)
    return render(request, 'members/clubmember_detail.html', {'clubmember': clubmember})


def remove_clubmember(request, clubmember_id):
    clubmember = get_object_or_404(ClubMember, pk=clubmember_id)
    clubmember.delete()
    return HttpResponseRedirect('/members/')
