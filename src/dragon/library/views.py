from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Book, Game, Item


class LibraryView(generic.ListView):
    template_name = 'library/library.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.order_by('name')


def book_detail(request: HttpRequest, book_id: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'library/book_detail.html', {'book': book})


def game_detail(request: HttpRequest, game_id: int) -> HttpResponse:
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'library/game_detail.html', {'game': game})


def book_form(request: HttpRequest) -> HttpResponse:
    return render(request, 'library/book_form.html')


def game_form(request: HttpRequest):
    return render(request, 'library/game_form.html')


def add_book(request: HttpRequest) -> HttpResponse:
    name = request.POST['name']
    if name != '':
        description = request.POST['description']
        notes = request.POST['notes']
        book = Book(name=name, description=description, notes=notes)
        book.save()
    return HttpResponseRedirect('/library/')


def add_game(request: HttpRequest):
    name = request.POST['name']
    if name != '':
        num_players = int(request.POST["players"])
        game = Game(name=name, players=num_players)
        game.save()
    return HttpResponseRedirect('/library/')


def remove_book(request: HttpRequest, book_id: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return HttpResponseRedirect('/library/')


def remove_game(request: HttpRequest, game_id: int) -> HttpResponse:
    game = get_object_or_404(Game, pk=game_id)
    game.delete()
    return HttpResponseRedirect('/library/')
