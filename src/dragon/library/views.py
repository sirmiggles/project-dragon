from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from .models import Book


def library(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    return render(request, 'library/library.html', {'books': books})


def book_detail(request: HttpRequest, book_id: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'library/book_detail.html', {'book': book})


def book_form(request: HttpRequest) -> HttpResponse:
    return render(request, 'library/book_form.html')


def add_book(request: HttpRequest) -> HttpResponse:
    book = Book(name=request.POST['name'], description=request.POST['description'], notes=request.POST['notes'])
    if book.name != '':
        book.save()
    return HttpResponseRedirect('/library/')


def remove_book(request: HttpRequest, book_id: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return HttpResponseRedirect('/library/')

def booksearch(request):
    template = "library\templates\library\library.html"
    query = request.Get.get('q')
    if query:
        results = Book.objects.filter(Q(BookName__icontains=query) | Q(ISBN__icontains=query))
    else:
        results = Book.objects.all()
    
    paginator = paginator(request,results,num=10)
    page = request.Get.get('page')
    
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    
    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index -7 if index >= 7 else 0
    end_index = index + 7 if index <= max_index - 7 else max_index
    page_range = paginator.page_range[start_index:end_index]
    
    context = {
        'items'= items,
        'page_range':page_range,
    }
    return render(request, template, context)
