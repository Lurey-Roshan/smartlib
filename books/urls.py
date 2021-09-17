from django.urls import path
from books import views
from books.views import BookListView
urlpatterns = [
    
    #path('', views.index, name='index'),
    path('create-level',views.create_level  ,name='create_level'),
    path('level/edit/<id>', views.edit_level , name='edit_level'),
    path('create-faculty',views.create_faculty  ,name='create_faculty'),
    path('create-program',views.create_program  ,name='create_program'),
    path('create-sem',views.create_sem  ,name='create_sem'),
    path('create-book',views.create_book  ,name='create_book'),
    path('<id>', views.book_detail , name='book_detail'),
    path('level-index', views.level_index, name='level_index'),
    path('edit/<id>', views.edit_book , name='edit_book'),
    path('delete/<id>', views.delete_book , name='delete_book'),
    #path('get_books',views.get_book, name='get_book')
    path('', BookListView.as_view(), name='index'),

    
]
#path('', views. , name=''),

#https://www.javatpoint.com/django-forms