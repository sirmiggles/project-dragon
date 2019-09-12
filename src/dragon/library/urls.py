from typing import List

from django.urls import path

from . import views

app_name = 'library'

urlpatterns: List[path] = [
    path('', views.LibraryView.as_view(), name='dragon'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('add_book/', views.add_book, name='add_book'),
    path('remove_book/<int:book_id>/', views.remove_book, name='remove_book'),
    path('book_form/', views.book_form, name='book_form'),
    path('game_form/',views.game_form, name = 'game_form'),
    path('add_game/', views.add_game, name='add_game')
]