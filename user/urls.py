from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('signup/', views.signup, name='signup'),
        path('login/', views.login, name='login'),
        path('board/', views.board, name='board'),
        path('register/', views.register, name='register'),
        path('logout/', views.logout, name='logout'),
        path('detail/', views.detail, name='detail'),
        path('whoami/', views.whoami, name='whoami'),
        
        


        ]
