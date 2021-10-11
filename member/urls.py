from django.urls import path

from member import	views



urlpatterns=[
	path('login', views.login_user, name='login'),
	path('register', views.register, name='register'),
	path('logout_user',views.logout_user, name='log_out'),
	path('users',views.users, name='users'),
	path('delete/<id>', views.user_delete, name='del_user'),
	path('user/<id>/edit', views.edit_user, name='edit_user'),
	path('mem/<id>/detail', views.user_detail, name='user_detail'),

	]