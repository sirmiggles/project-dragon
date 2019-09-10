from typing import List

from django.urls import path

from . import views

app_name = 'library'

urlpatterns: List[path] = [
    path('', views.library, name='dragon'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('add_book/', views.add_book, name='add_book'),
    path('remove_book/<int:book_id>', views.remove_book, name='remove_book'),
    path('book_form/', views.book_form, name='book_form')
]