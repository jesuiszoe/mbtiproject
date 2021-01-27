from django.urls import path
from . import views

urlpatterns = [
        path('board/', views.board),
        path('register/',views.register),
        path('', views.home),
        



        ]
