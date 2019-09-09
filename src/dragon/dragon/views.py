from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'dragon/index.html')


def faq(request: HttpRequest) -> HttpResponse:
    return render(request, 'dragon/faq.html')
