from django.urls import path
from home import views

urlpatterns = [
	path('',views.Home_page, name='home'),
	path('contact', views.contact, name='contact')


]
