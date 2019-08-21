from django.db.models import Manager
from django.shortcuts import render
from django.views import generic
from django.db import models
from .models import Book

# Create your views here.

def index(request):
    return render(request, 'page/index.html')

def page(request):
    return render(request, 'page/page.html')

def library(request):
    books = Book.objects.all().order_by('title')

    return render(request, 'page/library.html', {'books' : books})
