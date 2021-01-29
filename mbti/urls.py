"""mbti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import user.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mbti/', include('user.urls')),
    path('home/', user.views.home, name='home'),
    path('signup/', user.views.signup, name='signup'),
    path('login/', user.views.login, name='login'),
    path('logout/', user.views.logout, name='logout'),
    path('detail/<int:id>', user.views.detail, name='detail'),
    path('post/', user.views.post, name='post'),
    path('new/', user.views.new, name = 'new'),
    path('new/create', user.views.create, name='create'),
    path('enfp/', user.views.enfp, name='enfp'),
    path('isfj/', user.views.isfj, name='isfj'),
    path('infp/', user.views.infp, name='infp'),
    path('home/whoami/', user.views.whoami, name='whoami'),

   
]
