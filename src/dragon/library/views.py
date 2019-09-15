from django.db.models import BooleanField
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import BookForm, GameForm, CardForm
from .models import Book, Game, Tag, Card, Item


def library_view(request: HttpRequest) -> HttpResponse:
    books = Book.objects.order_by('name')
    games = Game.objects.order_by('name')
    cards = Card.objects.order_by('name')
    tags = Tag.objects.order_by('name')
    return render(request, 'library/library.html', {'books': books, 'games': games, 'cards': cards, 'tags': tags})


def book_detail(request: HttpRequest, book_id: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'library/book_detail.html', {'book': book})


def game_detail(request: HttpRequest, game_id: int) -> HttpResponse:
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'library/game_detail.html', {'game': game})


def card_detail(request: HttpRequest, card_id: int) -> HttpResponse:
    card = get_object_or_404(Card, pk=card_id)
    return render(request, 'library/card_detail.html', {'card': card})


def book_form(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, "library/book_form.html", {'form': form})


def game_form(request):
    form = GameForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, "library/game_form.html", {'form': form})


def card_form(request: HttpRequest) -> HttpResponse:
    form = CardForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, "library/card_form.html", {'form': form})


def tag_form(request: HttpRequest):
    return render(request, 'library/tag_form.html')


def add_book(request: HttpRequest) -> HttpResponse:
    name = request.POST['name']
    if name != '':
        description = request.POST['description']
        notes = request.POST['notes']
        condition = request.POST['condition']
        isbn = request.POST['isbn']
        book = Book(name=name, description=description, notes=notes, condition=condition, isbn=isbn)
        book.save()
    return HttpResponseRedirect('/library/')


def add_game(request: HttpRequest):
    name = request.POST['name']
    if name != '':
        minplayers = int(request.POST["minplayers"])
        maxplayers = int(request.POST["maxplayers"])
        mingamelength = request.POST["mingamelength"]
        maxgamelength = request.POST["maxgamelength"]
        condition = request.POST['condition']
        game = Game(name=name, maxplayers=maxplayers, minplayers=minplayers, condition=condition,
                    mingamelength=mingamelength, maxgamelength=maxgamelength)
        game.save()
    return HttpResponseRedirect('/library/')


def add_card(request: HttpRequest):
    name = request.POST['name']
    if name != '':
        deck_type = request.POST['deck_type']
        description = request.POST['description']
        condition = request.POST['condition']
        card = Card(name=name, deck_type=deck_type, description=description, condition=condition)
        card.save()
    return HttpResponseRedirect('/library/')


def add_tag(request: HttpRequest):
    name = request.POST['name']
    if name != '':
        tag = Tag(name=name)
        tag.save()
    return HttpResponseRedirect('/library/')


def remove_book(request: HttpRequest, book_id: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return HttpResponseRedirect('/library/')


def remove_game(request: HttpRequest, game_id: int) -> HttpResponse:
    game = get_object_or_404(Game, pk=game_id)
    game.delete()
    return HttpResponseRedirect('/library/')


def remove_card(request: HttpRequest, card_id: int) -> HttpResponse:
    card = get_object_or_404(Card, pk=card_id)
    card.delete()
    return HttpResponseRedirect('/library/')


def borrow_card(request: HttpRequest, card_id: int) -> HttpResponse:
    card = get_object_or_404(Card, pk=card_id)
    card.available = False
    card.save()
    # Item.available = BooleanField(False)
    return HttpResponseRedirect('/library/')

