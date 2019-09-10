from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

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
