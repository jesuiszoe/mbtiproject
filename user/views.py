from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import User
from django.contrib import auth
from django.contrib.auth.models import User



def home(request):
    return render(request,"home.html")

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password1']
            )

        signup = Signup()
        signup.name = request.POST['name']
        signup.user = user
        signup.save()
        auth.login(request, user)
        return redirect('home')
    return render(request, 'signup.html')


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')

def board(req):
    if req.method == "POST":
        title = req.POST['title']
        mbti = req.POST['mbti']
        body_text = req.POST['body_text']

        data = {'title':title, 'mbti':mbti, 'body_text':body_text}
        return render(req,"board.html",data)


    return render(req,'board.html')




def register(req):
    return render(req,'register.html')