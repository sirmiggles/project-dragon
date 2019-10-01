from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import ClubMember, NonMember
from .forms import ClubMemberForm, NonMemberForm


def members(request):
    clubmembers = ClubMember.objects.order_by('firstName')
    nonmembers = NonMember.objects.order_by('firstName')
    return render(request, 'members/members.html', {'clubmembers': clubmembers, 'nonmembers': nonmembers})


def clubmember_form(request):
    form = ClubMemberForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, "members/clubmember_form.html", {'form': form})


def nonmember_form(request):
    form = NonMemberForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, "members/nonmember_form.html", {'form': form})


def add_clubmember(request):
    firstName = request.POST['firstName']
    surname = request.POST['surname']
    preferredName = request.POST['preferredName']
    preferredPronoun = request.POST['preferredPronoun']
    guildMember = bool(request.POST['guildMember'])
    isStudent = bool(request.POST['isStudent'])
    universityID = request.POST['universityID']
    clubRank = request.POST['clubRank']
    email = request.POST['email']
    phoneNumber = request.POST['phoneNumber']
    joinDate = request.POST['joinDate']
    incidents = request.POST['incidents']

    if firstName != '':
        clubmember = ClubMember(firstName=firstName, surname=surname, preferredName=preferredName,
                                preferredPronoun=preferredPronoun, guildMember=guildMember, isStudent=isStudent,
                                universityID=universityID, clubRank=clubRank, email=email, phoneNumber=phoneNumber,
                                joinDate=joinDate, incidents=incidents
                                )
        clubmember.save()
    return HttpResponseRedirect('/members/')


def add_nonmember(request):
    firstName = request.POST['firstName']
    surname = request.POST['surname']
    email = request.POST['email']
    organization = request.POST['organization']
    phoneNumber= request.POST['phoneNumber']
    addedDate = request.POST['addedDate']
    incidents = request.POST['incidents']

    if firstName != '':
        nonmember = NonMember(firstName=firstName, surname=surname, email=email, phoneNumber=phoneNumber,
                              addedDate=addedDate, incidents=incidents, organization=organization
                              )
        nonmember.save()
    return HttpResponseRedirect('/members/')


def clubmember_detail(request, clubmember_id):
    clubmember = get_object_or_404(ClubMember, pk=clubmember_id)
    return render(request, 'members/clubmember_detail.html', {'clubmember': clubmember})


def nonmember_detail(request, nonmember_id):
    nonmember = get_object_or_404(NonMember, pk=nonmember_id)
    return render(request, 'members/nonmember_detail.html', {'nonmember': nonmember})


def remove_clubmember(request: HttpRequest, clubmember_id: int) -> HttpResponse:
    clubmember = get_object_or_404(ClubMember, pk=clubmember_id)
    clubmember.delete()
    return HttpResponseRedirect('/members/')


def remove_nonmember(request: HttpRequest, nonmember_id: int) -> HttpResponse:
    nonmember = get_object_or_404(NonMember, pk=nonmember_id)
    nonmember.delete()
    return HttpResponseRedirect('/members/')
