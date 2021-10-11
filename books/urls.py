from django.urls import path
from books import views
from django.contrib.auth.decorators import login_required
from books.views import BookListView
urlpatterns = [
    
    #path('', views.index, name='index'),
    #path('create-level',views.create_level  ,name='create_level'),
    #path('level/edit/<id>', views.edit_level , name='edit_level'),
    #path('create-faculty',views.create_faculty  ,name='create_faculty'),
    path('create-program',views.create_program  ,name='create_program'),
    #path('create-sem',views.create_sem  ,name='create_sem'),
    path('create-book',views.create_book  ,name='create_book'),
    path('details/<id>', views.book_detail , name='book_detail'),
    #path('level-index', views.level_index, name='level_index'),
    path('edit/<id>', views.edit_book , name='edit_book'),
    path('delete/<id>', views.delete_book , name='delete_book'),
    path('', login_required(BookListView.as_view()), name='index'),
    path('course',views.courses, name='course'),
    path('detail/<id>/view',views.view_pdf, name='view_pdf'),
    #path('image/<id>/view', views.view_image, name="view_image"),
    #path('level/<id>/delete', views.delete_level , name="delete_level"),
    #path('sem/<id>/delete', views.delete_sem , name="delete_sem"),
    path('program/<id>/delete', views.delete_program , name="delete_program"),
    path('program/<id>/edit', views.edit_program , name="edit_program"),
    path('program/<id>/detail', views.program_detail , name="program_detail"),
    #path('faculty/<id>/delete', views.delete_faculty , name="delete_faculty"),
    

    
]

