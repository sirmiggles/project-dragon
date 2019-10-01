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
