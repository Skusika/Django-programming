from django.contrib import admin
from django.urls import path
from . import views
from .views import register, profile, home, OneBook
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registration', register, name='register'),
    path('home', home, name='home'),
    path('profile', profile, name='profile'),
    path('login', auth_views.LoginView.as_view(template_name='my_library/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='my_library/logout.html'), name='logout'),
    path('book/<int:pk>', views.show_one_book, name='one_book'),
    path('all_book', views.show_all_book)
]
