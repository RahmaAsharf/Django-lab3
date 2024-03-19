
from django.urls import path
from library.views import home, base, list, profile, create_book, delete_book, update_book

urlpatterns = [
    path('home',home,name='home'),
    path('base',base,name='base'),
    path('list',list,name='list'),
    path('profile/<int:id>/',profile, name='profile'),
    path('add',create_book,name='create_book'),
    path('delete/<int:id>/',delete_book, name='delete'),
    path('update/<int:id>/',update_book, name='update')
]