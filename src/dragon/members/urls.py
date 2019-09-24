from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('', views.members, name='members'),
    path('clubmember_form/', views.user_form, name='user_form'),
    path('add_clubmember/', views.add_clubmember, name='add_user'),
    path('clubmember/<int:clubmember_id>/', views.clubmember_detail, name='user_detail'),
    path('remove_clubmember/<int:clubmember_id>/', views.remove_clubmember, name='remove_user')
]
