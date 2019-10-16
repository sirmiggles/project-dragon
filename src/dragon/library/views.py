from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import BookForm, GameForm, CardForm, TagForm, GenreForm, SeriesForm
from .models import Item, Book, Game, Card, Tag, Genre, Series, Borrow
from .views_library import ItemList
from django.contrib.auth.decorators import login_required, user_passes_test


def has_perm(self, perm, obj=None):
    try:
        user_perm = self.user_permissions.get(codename=perm)
    except ObjectDoesNotExist:
        user_perm = False
    if user_perm:
        return True
    else:
        return False


def permission_required(*perms):
    return user_passes_test(lambda u: any(u.has_perm(perm) for perm in perms), login_url='/')


# group restriction filter(not using)


def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""

    def in_groups(user):
        if user.is_authenticated:
            if bool(user.groups.filter(name__in=group_names)) | user.is_superuser:
                return True
        return False

    return user_passes_test(in_groups)


all_view = ItemList.as_view(
    model=Item, context_object_name="items", template_name="library/item/all.html")

book_view = ItemList.as_view(
    model=Book, context_object_name="books", template_name="library/book/all.html")

game_view = ItemList.as_view(
    model=Game, context_object_name="games", template_name="library/game/all.html")

cardgame_view = ItemList.as_view(
    model=Card, context_object_name="cards", template_name="library/cardgame/all.html")


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
        form.save()
        return HttpResponseRedirect('/library/ALL/')

    return render(request, 'library/tag/create_form.html', {'form': form})


def genre_form(request):
    form = GenreForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/library/ALL/')

    return render(request, 'library/genre/create_form.html', {'form': form})


def series_form(request):
    form = SeriesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/library/ALL/')

    return render(request, 'library/series/create_form.html', {'form': form})


# Added rendering for book editing, referring to the book id
@login_required(login_url='/')
@permission_required("library.change_book")
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
@login_required
@permission_required("library.change_game")
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
@login_required
@permission_required("library.change_card")
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


# Added rendering for tag editing, referring to the tag id
@login_required
@permission_required("library.change_tag")
def tag_edit_form(request: HttpRequest, tag_id: int) -> HttpResponse:
    tag = get_object_or_404(Tag, pk=tag_id)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            form.save_m2m()
            return HttpResponseRedirect('/library/ALL/')
    else:
        form = TagForm(instance=tag)

    return render(request, "library/tag/edit_form.html", {'tag': tag, 'form': form})


# Added rendering for genre editing, referring to the genre id
@login_required
@permission_required("library.change_genre")
def genre_edit_form(request: HttpRequest, genre_id: int) -> HttpResponse:
    genre = get_object_or_404(Genre, pk=genre_id)
    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            form.save_m2m()
            return HttpResponseRedirect('/library/ALL/')
    else:
        form = GenreForm(instance=genre)

    return render(request, "library/genre/edit_form.html", {'genre': genre, 'form': form})


# Added rendering for series editing, referring to the series id
@login_required
@permission_required("library.change_series")
def series_edit_form(request: HttpRequest, series_id: int) -> HttpResponse:
    series = get_object_or_404(Series, pk=series_id)
    if request.method == 'POST':
        form = SeriesForm(request.POST, instance=series)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            form.save_m2m()
            return HttpResponseRedirect('/library/ALL/')
    else:
        form = SeriesForm(instance=series)

    return render(request, "library/series/edit_form.html", {'series': series, 'form': form})


@login_required
@permission_required("library.delete_book")
def remove_book(request: HttpRequest, book_id: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return HttpResponseRedirect('/library/books')


@login_required
@permission_required("library.delete_game")
def remove_game(request: HttpRequest, game_id: int) -> HttpResponse:
    game = get_object_or_404(Game, pk=game_id)
    game.delete()
    return HttpResponseRedirect('/library/games')


@login_required
@permission_required("library.delete_card")
def remove_card(request: HttpRequest, card_id: int) -> HttpResponse:
    card = get_object_or_404(Card, pk=card_id)
    card.delete()
    return HttpResponseRedirect('/library/cardgames')


# Borrowing-related views
@permission_required("library.add_borrow")
def borrow_card(request: HttpRequest, card_id: int) -> HttpResponse:
    card = get_object_or_404(Card, pk=card_id)
    card.borrow_item()
    return HttpResponseRedirect('/library/cardgames')


@permission_required("library.add_borrow")
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
