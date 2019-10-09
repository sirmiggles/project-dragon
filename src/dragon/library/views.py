from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import BookForm, GameForm, CardForm
from .models import Book, Game, Tag, Card, Item, Borrow

from django.db.models import Q

# Viewing the Items table, ordered by the name
def all_view(request: HttpRequest) -> HttpResponse:
    
    searchterm = ''
    items = Item.objects.order_by('name')

    if 'search' in request.GET:
        searchterm = request.GET['search']
        itemsfilter = Q(name__icontains=searchterm)
        items = items.filter(itemsfilter)
    
    return render(request, 'library/item/all.html', {'items': items, 'searchterm': searchterm})


def book_view(request: HttpRequest) -> HttpResponse:
    
    searchterm = ''
    books = Book.objects.order_by('name')
    tags = Tag.objects.order_by('name')

    if 'search' in request.GET:
        searchterm = request.GET['search']
        booksfilter = Q(name__icontains=searchterm) | Q(isbn__icontains=searchterm)
        books = books.filter(booksfilter)
    
    return render(request, 'library/book/all.html', {'books': books, 'tags': tags, 'searchterm': searchterm})


def game_view(request: HttpRequest) -> HttpResponse:
    
    searchterm = ''
    games = Game.objects.order_by('name')
    tags = Tag.objects.order_by('name')

    if 'search' in request.GET:
        searchterm = request.GET['search']
        gamesfilter = Q(name__icontains=searchterm)
        games = games.filter(gamesfilter)

    return render(request, 'library/game/all.html', {'games': games, 'tags': tags, 'searchterm': searchterm})


def cardgame_view(request: HttpRequest) -> HttpResponse:
    
    searchterm = ''
    cards = Card.objects.order_by('name')
    tags = Tag.objects.order_by('name')

    if 'search' in request.GET:
        searchterm = request.GET['search']
        cardsfilter = Q(name__icontains=searchterm)
        cards = cards.filter(cardsfilter)

    return render(request, 'library/cardgame/all.html', {'cards': cards, 'tags': tags, 'searchterm': searchterm})


def book_detail(request: HttpRequest, book_id: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'library/book/detail.html', {'book': book})


def game_detail(request: HttpRequest, game_id: int) -> HttpResponse:
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'library/game/detail.html', {'game': game})


def card_detail(request: HttpRequest, card_id: int) -> HttpResponse:
    card = get_object_or_404(Card, pk=card_id)
    return render(request, 'library/cardgame/detail.html', {'card': card})


def book_form(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, "library/book/create_form.html", {'form': form})


def game_form(request):
    form = GameForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, "library/game/create_form.html", {'form': form})


def card_form(request: HttpRequest) -> HttpResponse:
    form = CardForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, "library/cardgame/create_form.html", {'form': form})


def tag_form(request: HttpRequest):
    return render(request, 'library/tag_form.html')


def add_book(request: HttpRequest) -> HttpResponse:
    name = request.POST['name']
    if name != '':
        description = request.POST['description']
        notes = request.POST['notes']
        condition = request.POST['condition']
        isbn = request.POST['isbn']
        edition = request.POST['edition']
        year = request.POST['year']
        genre = request.POST['genre']
        book = Book(name=name, description=description, notes=notes, condition=condition, isbn=isbn, year=year,
                    edition=edition, genre=genre)
        book.save()
    return HttpResponseRedirect('/library/books')


def add_game(request: HttpRequest):
    name = request.POST['name']
    if name != '':
        description = request.POST['description']
        notes = request.POST['notes']
        minplayers = int(request.POST["minplayers"])
        maxplayers = int(request.POST["maxplayers"])
        mingamelength = request.POST["mingamelength"]
        maxgamelength = request.POST["maxgamelength"]
        difficulty = request.POST['difficulty']
        genre = request.POST['genre']
        condition = request.POST['condition']
        game = Game(name=name, maxplayers=maxplayers, minplayers=minplayers, condition=condition,
                    mingamelength=mingamelength, maxgamelength=maxgamelength, difficulty=difficulty, genre=genre,
                    description=description, notes=notes)
        game.save()
    return HttpResponseRedirect('/library/games')


def add_card(request: HttpRequest):
    name = request.POST['name']
    if name != '':
        deck_type = request.POST['deck_type']
        description = request.POST['description']
        notes = request.POST['notes']
        minplayers = int(request.POST["minplayers"])
        maxplayers = int(request.POST["maxplayers"])
        mingamelength = request.POST["mingamelength"]
        maxgamelength = request.POST["maxgamelength"]
        difficulty = request.POST['difficulty']
        condition = request.POST['condition']
        card = Card(name=name, deck_type=deck_type, description=description, condition=condition, notes=notes,
                    maxplayers=maxplayers, minplayers=minplayers, mingamelength=mingamelength,
                    maxgamelength=maxgamelength, difficulty= difficulty)
        card.save()
    return HttpResponseRedirect('/library/cardgames')


def add_tag(request: HttpRequest):
    name = request.POST['name']
    if name != '':
        tag = Tag(name=name)
        tag.save()
    return HttpResponseRedirect('/library/books')


def update_book(request: HttpRequest, book_id: int):
    book = get_object_or_404(Book, pk=book_id)
    book.name = request.POST['name']
    if book.name != '':
        book.description = request.POST['description']
        book.notes = request.POST['notes']
        book.condition = request.POST['condition']
        book.isbn = request.POST['isbn']
        book.edition = request.POST['edition']
        book.year = request.POST['year']
        book.genre = request.POST['genre']
        book.save()
    return HttpResponseRedirect('/library/books')


# Added rendering for book editing, referring to the book id
def book_edit_form(request: HttpRequest, book_id: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=book_id)
    form = BookForm(instance=book)
    if form.is_valid():
        form.save()
    return render(request, "library/book/update_form.html", {'book': book, 'form': form})


def update_game(request: HttpRequest, game_id: int):
    game = get_object_or_404(Game, pk=game_id)
    game.name = request.POST['name']
    if game.name != '':
        game.description = request.POST['description']
        game.notes = request.POST['notes']
        game.condition = request.POST['condition']
        game.minplayers = request.POST['minplayers']
        game.maxplayers = request.POST['maxplayers']
        game.mingamelength = request.POST['mingamelength']
        game.maxgamelength = request.POST['maxgamelength']
        game.difficulty = request.POST['difficulty']
        game.genre = request.POST['genre']
        game.save()
    return HttpResponseRedirect('/library/games')


# Added rendering for game editing, referring to the game id
def game_edit_form(request: HttpRequest, game_id: int) -> HttpResponse:
    game = get_object_or_404(Game, pk=game_id)
    form = GameForm(instance=game)
    if form.is_valid():
        form.save()
    return render(request, "library/game/edit_form.html", {'game': game, 'form': form})


def update_card(request: HttpRequest, card_id: int):
    card = get_object_or_404(Card, pk=card_id)
    card.name = request.POST['name']
    if card.name != '':
        card.description = request.POST['description']
        card.notes = request.POST['notes']
        card.condition = request.POST['condition']
        card.minplayers = request.POST['minplayers']
        card.maxplayers = request.POST['maxplayers']
        card.mingamelength = request.POST['mingamelength']
        card.maxgamelength = request.POST['maxgamelength']
        card.difficulty = request.POST['difficulty']
        card.deck_type = request.POST['deck_type']
        card.save()
    return HttpResponseRedirect('/library/cardgames')


# Added rendering for game editing, referring to the game id
def card_edit_form(request: HttpRequest, card_id: int) -> HttpResponse:
    card = get_object_or_404(Card, pk=card_id)
    form = CardForm(instance=card)
    if form.is_valid():
        form.save()
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


def returned(request: HttpRequest, card_id: int) -> HttpResponse:
    loan = get_object_or_404(Borrow, item_id=card_id)
    loan.delete()
    return HttpResponseRedirect('/library/card/' + str(card_id))
