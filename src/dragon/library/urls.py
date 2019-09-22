from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.library_view, name='library'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('game/<int:game_id>/', views.game_detail, name='game_detail'),
    path('card/<int:card_id>/', views.card_detail, name='card_detail'),
    path('add_book/', views.add_book, name='add_book'),
    path('remove_book/<int:book_id>/', views.remove_book, name='remove_book'),
    path('remove_game/<int:game_id>/', views.remove_game, name='remove_game'),
    path('remove_card/<int:card_id>/', views.remove_card, name='remove_card'),
    path('book_form/', views.book_form, name='book_form'),
    path('game_form/', views.game_form, name='game_form'),
    path('card_form/', views.card_form, name='card_form'),
    path('add_game/', views.add_game, name='add_game'),
    path('add_card/', views.add_card, name='add_card'),
    path('tag_form', views.tag_form, name='tag_form'),
    path('add_tag', views.add_tag, name='add_tag'),
    path('borrow_card/<int:card_id>/', views.borrow_card, name='borrow_card'),
    path('borrowed/', views.borrowed, name='borrowed'),
]
