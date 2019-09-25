from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import ClubMember
from .forms import ClubMemberForm


def members(request):
    clubmembers = ClubMember.objects.order_by('firstName')
    nonmembers = NonMember.objects.order_by('firstName')
    return render(request, 'members/members.html', {'clubmembers': clubmembers})


def clubmember_form(request):
    form = ClubMemberForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, "members/clubmember_form.html", {'form': form})


def add_clubmember(request):
    firstName = request.POST['firstName']
    surname = request.POST['surname']
    preferredName= request.POST['preferredName']
    preferredPronoun= request.POST['preferredPronoun']
    guildMember= bool(request.POST['guildMember'])
    isStudent= bool(request.POST['isStudent'])
    universityID= request.POST['universityID']
    clubRank= request.POST['clubRank']
    email= request.POST['email']
    phoneNumber= request.POST['phoneNumber']
    joinDate = request.POST['joinDate']
    incidents= request.POST['incidents']


    if firstName != '':
        clubmember = ClubMember(firstName=firstName, surname=surname, preferredName=preferredName,
                                preferredPronoun=preferredPronoun, guildMember=guildMember, isStudent=isStudent,
                                universityID=universityID, clubRank=clubRank, email=email, phoneNumber=phoneNumber,
                                joinDate=joinDate, incidents=incidents
                                )
        clubmember.save()
    return HttpResponseRedirect('/members/')


def clubmember_detail(request, clubmember_id):
    clubmember = get_object_or_404(ClubMember, pk=clubmember_id)
    return render(request, 'members/clubmember_detail.html', {'clubmember': clubmember})


def remove_clubmember(request, clubmember_id):
    clubmember = get_object_or_404(ClubMember, pk=clubmember_id)
    clubmember.delete()
    return HttpResponseRedirect('/members/')
