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
<<<<<<< HEAD
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
=======
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
>>>>>>> 1697ce4919f1e0add7320cdf526e02904bf1abf9


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
