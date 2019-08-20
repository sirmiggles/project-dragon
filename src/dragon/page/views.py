from django.shortcuts import render
from django.views import generic

# Create your views here.

def index(request):
    return render(request, 'page/index.html')

def page(request):
    return render(request, 'page/page.html')

def library(request):
    # todo: get a list of books and give to template

    return render(request, 'page/library.html')
