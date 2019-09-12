from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('', views.members, name='members'),
    path('user_form/', views.user_form, name='user_form'),
    path('add_user/', views.add_user, name='add_user')
]
