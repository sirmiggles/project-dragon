from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('clubmembers/', views.clubmembers, name='clubmembers'),
    path('clubmember_form/', views.clubmember_form, name='clubmember_form'),
    path('add_clubmember/', views.add_clubmember, name='add_clubmember'),
    path('clubmember/<int:clubmember_id>/', views.clubmember_detail, name='clubmember_detail'),
    path('clubmember_edit_form/<int:clubmember_id>/', views.clubmember_edit_form, name='clubmember_edit_form'),
    path('update_clubmember/<int:clubmember_id>/', views.update_clubmember, name='update_clubmember'),
    path('remove_clubmember/<int:clubmember_id>/', views.remove_clubmember, name='remove_clubmember'),

    path('nonmembers/', views.nonmembers, name='nonmembers'),
    path('nonmember_form/', views.nonmember_form, name='nonmember_form'),
    path('add_nonmember/', views.add_nonmember, name='add_nonmember'),
    path('nonmember/<int:nonmember_id>/', views.nonmember_detail, name='nonmember_detail'),
    path('nonmember_edit_form/<int:nonmember_id>/', views.nonmember_edit_form, name='nonmember_edit_form'),
    path('update_nonmember/<int:nonmember_id>/', views.update_nonmember, name='update_nonmember'),
    path('remove_nonmember/<int:nonmember_id>/', views.remove_nonmember, name='remove_nonmember')
]
