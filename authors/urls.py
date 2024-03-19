from django.urls import path
from authors.views import home , list ,create_author, profile, edit_author , delete_author

urlpatterns = [
    path('home',home,name='homeauthors'),
    path('list',list,name='listauthors'),
    path('add',create_author,name='create_author'),
    path('profile/<int:id>/',profile, name='authorprofile'),
    path('edit/<int:id>/',edit_author, name='edit_author'),
    path('delete/<int:id>/',delete_author, name='delete_author')

]