from django.contrib import admin
from django.urls import path
from . import views
from .models import Post

urlpatterns = [
        path('home', views.home, name='home'),
        path('signup/', views.signup, name='signup'),
        path('login/', views.login, name='login'),
        path('logout/', views.logout, name='logout'),
        path('detail/<int:id>', views.detail, name='detail'),
        path('post/', views.show_post, name='post'),
        path('new/', views.new, name = 'new'),
        path('new/create', views.create, name='create'),

        ]
