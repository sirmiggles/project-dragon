from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import BookForm, GameForm, CardForm
from .models import Book, Game, Tag, Card, Item, Borrow, Genre


# Viewing the Items table, ordered by the name
def all_view(request: HttpRequest) -> HttpResponse:
    items = Item.objects.order_by('name')
    tags = Tag.objects.order_by('name')
    genres = Genre.objects.order_by('name')
    return render(request, 'library/item/all.html', {'items': items, 'tags': tags, 'genres': genres})


def book_view(request: HttpRequest) -> HttpResponse:
    books = Book.objects.order_by('name')
    tags = Tag.objects.order_by('name')
    genres = Genre.objects.order_by('name')
    return render(request, 'library/book/all.html', {'books': books, 'tags': tags, 'genres': genres})


def game_view(request: HttpRequest) -> HttpResponse:
    games = Game.objects.order_by('name')
    tags = Tag.objects.order_by('name')
    genres = Genre.objects.order_by('name')
    return render(request, 'library/game/all.html', {'games': games, 'tags': tags, 'genres': genres})


def cardgame_view(request: HttpRequest) -> HttpResponse:
    cards = Card.objects.order_by('name')
    tags = Tag.objects.order_by('name')
    genres = Genre.objects.order_by('name')
    return render(request, 'library/cardgame/all.html', {'cards': cards, 'tags': tags, 'genres': genres})


def book_detail(request: HttpRequest, book_id: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=book_id)
    tags = book.tags.all()
    genres = book.genres.all()
    return render(request, 'library/book/detail.html', {'book': book, 'tags': tags, 'genres': genres})


def game_detail(request: HttpRequest, game_id: int) -> HttpResponse:
    game = get_object_or_404(Game, pk=game_id)
    tags = game.tags.all()
    genres = game.genres.all()
    return render(request, 'library/game/detail.html', {'game': game, 'tags': tags, 'genres': genres})


def card_detail(request: HttpRequest, card_id: int) -> HttpResponse:
    card = get_object_or_404(Card, pk=card_id)
    tags = card.tags.all()
    genres = card.genres.all()
    return render(request, 'library/cardgame/detail.html', {'card': card, 'tags': tags, 'genres': genres})


def book_form(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        book = form.save(commit=False)
        book.save()
        form.save_m2m()
        return HttpResponseRedirect('/library/books/')

    return render(request, "library/book/create_form.html", {'form': form})


def game_form(request):
    form = GameForm(request.POST or None)
    if form.is_valid():
        game = form.save(commit=False)
        game.save()
        form.save_m2m()
        return HttpResponseRedirect('/library/games/')

    return render(request, "library/game/create_form.html", {'form': form})


def card_form(request):
    form = CardForm(request.POST or None)
    if form.is_valid():
        card = form.save(commit=False)
        card.save()
        form.save_m2m()
        return HttpResponseRedirect('/library/cardgames/')

    return render(request, "library/cardgame/create_form.html", {'form': form})


def tag_form(request):
    form = TagForm(request.POST or None)
    if form.is_valid():
        tag = form.save(commit=False)
        tag.save()
        return HttpResponseRedirect('/library/ALL/')

    return render(request, 'library/tag/tag_form.html', {'form: form'})


def genre_form(request):
    form = GenreForm(request.POST or None)
    if form.is_valid():
        genre = form.save(commit=False)
        genre.save()
        return HttpResponseRedirect('/library/ALL/')

    return render(request, 'library/genre/genre_form.html', {'form: form'})


# Added rendering for book editing, referring to the book id
def book_edit_form(request: HttpRequest, book_id: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            form.save_m2m()
            return HttpResponseRedirect('/library/books/')
    else:
        form = BookForm(instance=book)

    return render(request, "library/book/edit_form.html", {'book': book, 'form': form})


# Added rendering for game editing, referring to the game id
def game_edit_form(request: HttpRequest, game_id: int) -> HttpResponse:
    game = get_object_or_404(Game, pk=game_id)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            form.save_m2m()
            return HttpResponseRedirect('/library/games/')
    else:
        form = GameForm(instance=game)

    return render(request, "library/game/edit_form.html", {'game': game, 'form': form})


# Added rendering for card game editing, referring to the card game id
def card_edit_form(request: HttpRequest, card_id: int) -> HttpResponse:
    card = get_object_or_404(Card, pk=card_id)
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            form.save_m2m()
            return HttpResponseRedirect('/library/cardgames/')
    else:
        form = CardForm(instance=card)

    return render(request, "library/cardgame/edit_form.html", {'card': card, 'form': form})


def remove_book(request: HttpRequest, book_id: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return HttpResponseRedirect('/library/books')


def remove_game(request: HttpRequest, game_id: int) -> HttpResponse:
    game = get_object_or_404(Game, pk=game_id)
    game.delete()
    return HttpResponseRedirect('/library/games')


def remove_card(request: HttpRequest, card_id: int) -> HttpResponse:
    card = get_object_or_404(Card, pk=card_id)
    card.delete()
    return HttpResponseRedirect('/library/cardgames')


# Borrowing-related views

def borrow_card(request: HttpRequest, card_id: int) -> HttpResponse:
    card = get_object_or_404(Card, pk=card_id)
    card.borrow_item()
    return HttpResponseRedirect('/library/cardgames')


def borrowed(request: HttpRequest):
    books = Book.objects.order_by('name')
    games = Game.objects.order_by('name')
    cards = Card.objects.order_by('name')
    tags = Tag.objects.order_by('name')
    return render(request, 'library/borrowed.html', {'books': books, 'games': games, 'cards': cards, 'tags': tags})


def borrow_detail(request: HttpRequest, card_id: int) -> HttpResponse:
    card = get_object_or_404(Card, pk=card_id)
    return render(request, 'library/borrow_detail.html', {'card': card})


def returned(request: HttpRequest, item_id: int) -> HttpResponse:
    loan = get_object_or_404(Borrow, item_id=item_id)
    loan.delete()
    return HttpResponseRedirect('/library/card/' + str(item_id))
