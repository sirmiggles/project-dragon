from django.urls import path
from . import views

app_name = 'library'

# the urls to access library pages

urlpatterns = [

    # Urls for items library page
    path('ALL/', views.all_view, name='ALL'),

    # Urls for book library page
    path('books/', views.book_view, name='books'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book_form/', views.book_form, name='book_form'),
    path('book_edit_form/<int:book_id>/', views.book_edit_form, name='book_edit_form'),
    path('remove_book/<int:book_id>/', views.remove_book, name='remove_book'),

    # Urls for game library page
    path('games/', views.game_view, name='games'),
    path('game/<int:game_id>/', views.game_detail, name='game_detail'),
    path('game_form/', views.game_form, name='game_form'),
    path('game_edit_form/<int:game_id>/', views.game_edit_form, name='game_edit_form'),
    path('remove_game/<int:game_id>/', views.remove_game, name='remove_game'),

    # Urls for card game library page
    path('cardgames/', views.cardgame_view, name='cardgames'),
    path('card/<int:card_id>/', views.card_detail, name='card_detail'),
    path('card_form/', views.card_form, name='card_form'),
    path('card_edit_form/<int:card_id>/', views.card_edit_form, name='card_edit_form'),
    path('remove_card/<int:card_id>/', views.remove_card, name='remove_card'),

    # Urls for tags
    path('tag_form/', views.tag_form, name='tag_form'),
    path('tag_edit_form/<int:tag_id>/', views.tag_edit_form, name='tag_edit_form'),

    # Urls for genres
    path('genre_form/', views.genre_form, name='genre_form'),
    path('genre_edit_form/<int:genre_id>/', views.genre_edit_form, name='genre_edit_form'),

    # Urls for series
    path('series_form/', views.series_form, name='series_form'),
    path('series_edit_form/<int:series_id>/', views.series_edit_form, name='series_edit_form'),

    # Urls for borrowing
    path('borrow_card/<int:card_id>/', views.borrow_card, name='borrow_card'),
    path('returned/<int:card_id>/', views.returned, name='returned'),
    path('borrow_detail/<int:card_id>/', views.borrow_detail, name='borrow_detail'),
    path('borrowed/', views.borrowed, name='borrowed'),
]
