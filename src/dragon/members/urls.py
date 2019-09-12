from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('', views.members, name='members'),
    path('user_form/', views.user_form, name='user_form'),
    path('add_user/', views.add_user, name='add_user'),
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
    path('remove_user/<int:user_id>/', views.remove_user, name='remove_user')
]
