
from django.contrib import admin
from django.urls import path
from .views import index,profile, editprofile,addphoto,delete_photo,search

urlpatterns = [
    path('', index, name='index'),
    path('edit-profile/', editprofile, name = 'editprofile'),
    path('add-post', addphoto, name = 'addphoto'),
    path('deletephoto/', delete_photo, name= 'deletephoto'),
    path('search/', search,name='search'),
    path('<str:username>/',profile, name='profile'),
]

