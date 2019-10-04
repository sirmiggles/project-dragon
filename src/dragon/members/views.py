from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import ClubMember, NonMember
from .forms import ClubMemberForm, NonMemberForm

from django.db.models import Q

from django.contrib.auth import authenticate,login,logout


def clubmembers(request):

    searchterm = ''
    clubmembers = ClubMember.objects.order_by('firstName')

    if 'search' in request.GET:
        searchterm = request.GET['search']
        clubmemberfilters = Q(firstName__icontains=searchterm) | Q(surname__icontains=searchterm) | \
                  Q(preferredName__icontains=searchterm)
        clubmembers = clubmembers.filter(clubmemberfilters)

    return render(request, 'members/clubmembers.html', {'clubmembers': clubmembers, 'searchterm': searchterm})


def nonmembers(request):

    searchterm = ''
    nonmembers = NonMember.objects.order_by('firstName')

    if 'search' in request.GET:
        searchterm = request.GET['search']
        nonmemberfilters = Q(firstName__icontains=searchterm) | Q(surname__icontains=searchterm)
        nonmembers = nonmembers.filter(nonmemberfilters)

    return render(request, 'members/nonmembers.html', {'nonmembers': nonmembers, 'searchterm': searchterm})


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
    password = request.POST['password']
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
        clubmember = ClubMember(firstName=firstName, surname=surname, password=password,preferredName=preferredName,
                                preferredPronoun=preferredPronoun, guildMember=guildMember, isStudent=isStudent,
                                universityID=universityID, clubRank=clubRank, email=email, phoneNumber=phoneNumber,
                                joinDate=joinDate, incidents=incidents
                                )
        clubmember.save()
    return HttpResponseRedirect('/members/clubmembers/')


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
    return HttpResponseRedirect('/members/nonmembers/')


def clubmember_detail(request, clubmember_id):
    clubmember = get_object_or_404(ClubMember, pk=clubmember_id)
    return render(request, 'members/clubmember_detail.html', {'clubmember': clubmember})


def nonmember_detail(request, nonmember_id):
    nonmember = get_object_or_404(NonMember, pk=nonmember_id)
    return render(request, 'members/nonmember_detail.html', {'nonmember': nonmember})


def remove_clubmember(request: HttpRequest, clubmember_id: int) -> HttpResponse:
    clubmember = get_object_or_404(ClubMember, pk=clubmember_id)
    clubmember.delete()
    return HttpResponseRedirect('/members/clubmembers/')


def remove_nonmember(request: HttpRequest, nonmember_id: int) -> HttpResponse:
    nonmember = get_object_or_404(NonMember, pk=nonmember_id)
    nonmember.delete()
    return HttpResponseRedirect('/members/nonmembers/')

def login(request):
    if request.method =='POST':
        firstName = request.POST['firstName']
        password = request.POST['password']
        
        user = authenticate(firstName=firstName,password=password)
        if user is not None:
            authenticate.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'members/login.html')
    
def logout(request):
    authenticate.logout(request)
    return redirect('/')
