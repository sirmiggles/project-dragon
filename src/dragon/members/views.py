from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import ClubMember, NonMember
from .forms import ClubMemberForm, NonMemberForm

from django.db.models import Q


def clubmembers(request):

    searchterm = ''
    clubmembers = ClubMember.objects.order_by('firstName')

    if 'search' in request.GET:
        searchterm = request.GET['search']
        clubmemberfilters = Q(firstName__icontains=searchterm) | Q(surname__icontains=searchterm) | \
                  Q(preferredName__icontains=searchterm)
        clubmembers = clubmembers.filter(clubmemberfilters)

    return render(request, 'members/all.html', {'clubmembers': clubmembers, 'searchterm': searchterm})


def nonmembers(request):

    searchterm = ''
    nonmembers = NonMember.objects.order_by('firstName')

    if 'search' in request.GET:
        searchterm = request.GET['search']
        nonmemberfilters = Q(firstName__icontains=searchterm) | Q(surname__icontains=searchterm)
        nonmembers = nonmembers.filter(nonmemberfilters)

    return render(request, 'members/all.html', {'nonmembers': nonmembers, 'searchterm': searchterm})


def clubmember_form(request):
    form = ClubMemberForm(request.POST or None)
    if form.is_valid():
        member = form.save(commit=False)
        member.save()
        form.save_m2m()
        return HttpResponseRedirect('/members/clubmembers/')

    return render(request, "members/clubmembers/create_form.html", {'form': form})


def nonmember_form(request):
    form = NonMemberForm(request.POST or None)
    if form.is_valid():
        nonmember = form.save(commit=False)
        nonmember.save()
        form.save_m2m()
        return HttpResponseRedirect('/members/nonmembers/')

    return render(request, "members/nonmembers/create_form.html", {'form': form})


def clubmember_detail(request, clubmember_id):
    clubmember = get_object_or_404(ClubMember, pk=clubmember_id)
    return render(request, 'members/detail.html', {'clubmember': clubmember})


def nonmember_detail(request, nonmember_id):
    nonmember = get_object_or_404(NonMember, pk=nonmember_id)
    return render(request, 'members/detail.html', {'nonmember': nonmember})


# Added rendering for clubmember editing, referring to the clubmember id
def clubmember_edit_form(request: HttpRequest, clubmember_id: int) -> HttpResponse:
    clubmember = get_object_or_404(ClubMember, pk=clubmember_id)
    if request.method == 'POST':
        form = ClubMemberForm(request.POST, instance=clubmember)
        if form.is_valid():
            member = form.save(commit=False)
            member.save()
            form.save_m2m()
            return HttpResponseRedirect('/members/clubmembers/')
    else:
        form = ClubMemberForm(instance=clubmember)

    return render(request, "members/clubmembers/edit_form.html", {'clubmember': clubmember, 'form': form})


# Added rendering for nonmember editing, referring to the nonmember id
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


def remove_clubmember(request: HttpRequest, clubmember_id: int) -> HttpResponse:
    clubmember = get_object_or_404(ClubMember, pk=clubmember_id)
    clubmember.delete()
    return HttpResponseRedirect('/members/clubmembers/')


def remove_nonmember(request: HttpRequest, nonmember_id: int) -> HttpResponse:
    nonmember = get_object_or_404(NonMember, pk=nonmember_id)
    nonmember.delete()
    return HttpResponseRedirect('/members/nonmembers/')
