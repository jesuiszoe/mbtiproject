from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import User
from django.contrib import auth


def home(request):
    return render(request,"user/home.html")

def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'user/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('user/home.html')
        else:
            return render(request, 'user/signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'user/signup.html')
    if not ( userid and username and password and gender):
   data['error'] = '모든 값을 입력해주세요.'
def register(req):
    return render(req,"register.html")

def board(req):
    if req.method == "POST":
        mbti = req.POST['mbti']
        title = req.POST['title']
        body_text = req.POST['body_text']
        

        data = {'mbti':mbti, 'title':title, 'body_text':body_text}
        return render(req,"board.html",data)
    return render(req,"board.html")


# Create your views here.
