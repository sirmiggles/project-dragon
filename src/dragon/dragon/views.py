from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# views are methods that are called when a HTTP request is sent to the server
# these requests are specified in the `urls.py` file


def index(request: HttpRequest) -> HttpResponse:
    """The main page for the website"""
    return render(request, 'dragon/index.html')

def faq(request: HttpRequest) -> HttpResponse:
    """An FAQ page for the website"""
    return render(request, 'dragon/faq.html')

def committee(request: HttpRequest) -> HttpResponse:
    """A committee page for the website"""
    return render(request, 'dragon/committee.html')

def contactus(request: HttpRequest) -> HttpResponse:
    """A contact-us page for the website"""
    return render(request, 'dragon/contact-us.html')

def roleplaying(request: HttpRequest) -> HttpResponse:
    """A roleplay information page for the website"""
    return render(request, 'dragon/roleplaying.html')

def lifemembers(request:HttpRequest) -> HttpResponse:
    """A life members information page for the website"""
    return render(request, 'dragon/life-members.html')