from django.urls import path
from . import views
from . import views_library

app_name = 'library'
from .models import Item, Book, Game, Card

# the urls to access library pages

urlpatterns = [

    # Urls for items library page
    path('ALL/', views_library.ItemList.as_view(model=Item, context_object_name="items",
                                                template_name="library/item/all.html"), name='ALL'),

    # Urls for book library page
    path('books/', views_library.ItemList.as_view(model=Book, context_object_name="books",
                                                  template_name="library/book/all.html"), name='books'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book_form/', views.book_form, name='book_form'),
    path('book_edit_form/<int:book_id>/', views.book_edit_form, name='book_edit_form'),
    path('remove_book/<int:book_id>/', views.remove_book, name='remove_book'),

    # Urls for game library page
    path('games/', views_library.ItemList.as_view(model=Game, context_object_name="games",
                                                  template_name="library/game/all.html"), name='games'),
    path('game/<int:game_id>/', views.game_detail, name='game_detail'),
    path('game_form/', views.game_form, name='game_form'),
    path('game_edit_form/<int:game_id>/', views.game_edit_form, name='game_edit_form'),
    path('remove_game/<int:game_id>/', views.remove_game, name='remove_game'),

    # Urls for card game library page
    path('cardgames/', views_library.ItemList.as_view(model=Card, context_object_name="cards",
                                                      template_name="library/cardgame/all.html"), name='cardgames'),
    path('card/<int:card_id>/', views.card_detail, name='card_detail'),
    path('card_form/', views.card_form, name='card_form'),
    path('card_edit_form/<int:card_id>/', views.card_edit_form, name='card_edit_form'),
    path('remove_card/<int:card_id>/', views.remove_card, name='remove_card'),

    # Urls for tags and genres
    path('tag_form/', views.tag_form, name='tag_form'),
    path('genre_form/', views.genre_form, name='genre_form'),

    # Urls for borrowing
    path('borrow_card/<int:card_id>/', views.borrow_card, name='borrow_card'),
    path('returned/<int:card_id>/', views.returned, name='returned'),
    path('borrow_detail/<int:card_id>/', views.borrow_detail, name='borrow_detail'),
    path('borrowed/', views.borrowed, name='borrowed')
]
