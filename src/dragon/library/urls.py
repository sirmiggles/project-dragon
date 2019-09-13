from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.library_view, name='library'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('game/<int:game_id>', views.game_detail, name='game_detail'),
    path('add_book/', views.add_book, name='add_book'),
    path('remove_book/<int:book_id>/', views.remove_book, name='remove_book'),
    path('remove_game/<int:game_id>/', views.remove_game, name='remove_game'),
    path('book_form/', views.book_form, name='book_form'),
    path('game_form/', views.game_form, name='game_form'),
    path('add_game/', views.add_game, name='add_game'),
    path('tag_form', views.tag_form, name='tag_form'),
    path('add_tag', views.add_tag, name='add_tag')
]
