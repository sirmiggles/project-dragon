from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import ClubMember, NonMember
from .forms import ClubMemberForm, NonMemberForm

from django.db.models import Q

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,auth,Group,Permission,ContentType
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages

#Group permission filter(not using but could be used in the future)
def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""

    def in_groups(user):
        if user.is_authenticated:
            if bool(user.groups.filter(name__in=group_names)) | user.is_superuser:
                return True
        return False
    return user_passes_test(in_groups)


def has_perm(self, perm, obj=None):
    try:
        user_perm = self.user_permissions.get(codename=perm)
    except ObjectDoesNotExist:
        user_perm = False
    if user_perm:
        return True
    else:
        return False
def permission_required(*perms):
    return user_passes_test(lambda u: any(u.has_perm(perm) for perm in perms), login_url='/')

@login_required(login_url='/')
@permission_required("members.delete_clubmember", "members.change_clubmember", "members.view_clubmember")
def clubmembers(request):

    searchterm = ''
    clubmembers = ClubMember.objects.order_by('FirstName')

    if 'search' in request.GET:
        searchterm = request.GET['search']
        clubmemberfilters = Q(FirstName__icontains=searchterm) | Q(surname__icontains=searchterm) | \
                  Q(preferredName__icontains=searchterm)
        clubmembers = clubmembers.filter(clubmemberfilters)

    return render(request, 'members/clubmembers/all.html', {'clubmembers': clubmembers, 'searchterm': searchterm})


@login_required
@permission_required("members.delete_nonmember", "members.change_nonmember", "members.view_nonmember")
def nonmembers(request):

    searchterm = ''
    nonmembers = NonMember.objects.order_by('FirstName')

    if 'search' in request.GET:
        searchterm = request.GET['search']
        nonmemberfilters = Q(FirstName__icontains=searchterm) | Q(surname__icontains=searchterm)
        nonmembers = nonmembers.filter(nonmemberfilters)

    return render(request, 'members/nonmembers/all.html', {'nonmembers': nonmembers, 'searchterm': searchterm})


@login_required
@permission_required("members.add_clubmember")
def clubmember_form(request):
    form = ClubMemberForm(request.POST or None)
    if form.is_valid():
        member = form.save(commit=False)
        member.save()
        form.save_m2m()
        return HttpResponseRedirect('/members/clubmembers/')

    return render(request, "members/clubmembers/create_form.html", {'form': form})


@login_required
@permission_required("members.add_nonmember")
def nonmember_form(request):
    form = NonMemberForm(request.POST or None)
    if form.is_valid():
        nonmember = form.save(commit=False)
        nonmember.save()
        form.save_m2m()
        return HttpResponseRedirect('/members/nonmembers/')
    return render(request, "members/nonmembers/create_form.html", {'form': form})

@login_required
@permission_required("members.add_clubmember")
def add_clubmember(request):
    FirstName= request.POST['FirstName']
    surname = request.POST['surname']
    password = request.POST['password']
    preferredName = request.POST['preferredName']
    preferredPronoun = request.POST['preferredPronoun']
    guildMember = bool(request.POST['guildMember'])
    isStudent = bool(request.POST['isStudent'])
    universityID = request.POST['universityID']
    email = request.POST['email']
    phoneNumber = request.POST['phoneNumber']
    joinDate = request.POST['joinDate']
    incidents = request.POST['incidents']

    if FirstName != '':
        clubmember = ClubMember(FirstName=FirstName, surname=surname, password=password, preferredName=preferredName,
                                preferredPronoun=preferredPronoun, guildMember=guildMember, isStudent=isStudent,
                                universityID=universityID, email=email, phoneNumber=phoneNumber,
                                joinDate=joinDate, incidents=incidents
                                )
        clubmember.save()
    return HttpResponseRedirect('/members/clubmembers/')

@login_required
@permission_required("members.add_nonmember")
def add_nonmember(request):
    FirstName = request.POST['FirstName']
    surname = request.POST['surname']
    email = request.POST['email']
    organization = request.POST['organization']
    phoneNumber= request.POST['phoneNumber']
    addedDate = request.POST['addedDate']
    incidents = request.POST['incidents']

    if FirstName != '':
        nonmember = NonMember(FirstName=FirstName, surname=surname, email=email, phoneNumber=phoneNumber,
                              addedDate=addedDate, incidents=incidents, organization=organization
                              )
        nonmember.save()
    return HttpResponseRedirect('/members/nonmembers/')

@login_required
@permission_required("members.view_clubmember")
def clubmember_detail(request, clubmember_id):
    clubmember = get_object_or_404(ClubMember, pk=clubmember_id)
    return render(request, 'members/clubmembers/detail.html', {'clubmember': clubmember})


@login_required
@permission_required("members.view_nonmember")
def nonmember_detail(request, nonmember_id):
    nonmember = get_object_or_404(NonMember, pk=nonmember_id)
    return render(request, 'members/nonmember_detail.html', {'nonmember': nonmember})

@login_required
@permission_required("members.change_clubmember")
def update_clubmember(request: HttpRequest, clubmember_id: int):
    clubmember = get_object_or_404(ClubMember, pk=clubmember_id)
    clubmember.FirstName = request.POST['FirstName']
    if clubmember.FirstName != '':
        clubmember.surname = request.POST['surname']
        clubmember.email = request.POST['email']
        clubmember.phoneNumber = request.POST['phoneNumber']
        clubmember.password = request.POST['password']
        clubmember.preferredName = request.POST['preferredName']
        clubmember.preferredPronoun = request.POST['preferredPronoun']
        clubmember.guildMember = bool(request.POST['guildMember'])
        clubmember.isStudent = bool(request.POST['isStudent'])
        clubmember.universityID = request.POST['universityID']
        clubmember.joinDate = request.POST['joinDate']
        clubmember.incidents = request.POST['incidents']
        clubmember.save()
    return HttpResponseRedirect('/members/clubmembers')


# Added rendering for clubmember editing, referring to the clubmember id
@login_required
@permission_required("members.change_clubmember")
def clubmember_edit_form(request: HttpRequest, clubmember_id: int) -> HttpResponse:
    clubmember = get_object_or_404(ClubMember, pk=clubmember_id)
    form = ClubMemberForm(instance=clubmember)
    if form.is_valid():
        form.save()
    return render(request, "members/clubmember_edit_form.html", {'clubmember': clubmember, 'form': form})

@login_required
@permission_required("members.change_nonmember")
def update_nonmember(request: HttpRequest, nonmember_id: int):
    nonmember = get_object_or_404(NonMember, pk=nonmember_id)
    nonmember.FirstName = request.POST['FirstName']
    if nonmember.FirstName != '':
        nonmember.surname = request.POST['surname']
        nonmember.email = request.POST['email']
        nonmember.phoneNumber = request.POST['phoneNumber']
        nonmember.organization = request.POST['organization']
        nonmember.addedDate = request.POST['addedDate']
        nonmember.incidents = request.POST['incidents']
        nonmember.save()
    return HttpResponseRedirect('/members/nonmembers')


# Added rendering for nonmember editing, referring to the nonmember id
@login_required
@permission_required("members.change_nonmember")
def nonmember_edit_form(request: HttpRequest, nonmember_id: int) -> HttpResponse:
    nonmember = get_object_or_404(NonMember, pk=nonmember_id)
    if request.method == 'POST':
        form = NonMemberForm(request.POST, instance=nonmember)
        if form.is_valid():
            nonmember = form.save(commit=False)
            nonmember.save()
            form.save_m2m()
            return HttpResponseRedirect('/members/nonmembers/')
    else:
        form = NonMemberForm(instance=nonmember)

    return render(request, "members/nonmembers/edit_form.html", {'nonmember': nonmember, 'form': form})


@login_required
@permission_required("members.delete_clubmember")
def remove_clubmember(request: HttpRequest, clubmember_id: int) -> HttpResponse:
    clubmember = get_object_or_404(ClubMember, pk=clubmember_id)
    clubmember.delete()
    return HttpResponseRedirect('/members/clubmembers/')


@login_required
@permission_required("members.delete_nonmember")
def remove_nonmember(request: HttpRequest, nonmember_id: int) -> HttpResponse:
    nonmember = get_object_or_404(NonMember, pk=nonmember_id)
    nonmember.delete()
    return HttpResponseRedirect('/members/nonmembers/')


def signin(request):
    if request.method =='POST':
        username= request.POST['FirstName']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/')
            print('Logged in')
        else:
            messages.error(request, "Error")
            return HttpResponseRedirect('/members/signin/')
    else:
        return render(request, 'members/signin.html')


@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect('/')
