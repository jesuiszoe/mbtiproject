from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import User
from django.contrib import auth
from django.contrib.auth.models import User
from django.utils import timezone
from .models import *


def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'], 
                password=request.POST['password1'],
                )
        signup = Signup()
        signup.user = user
        
        signup.save()
        auth.login(request, user)
        return redirect('home')
    return render(request, 'signup.html')





# Create your views here.



	
def login(request):
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'detail.html', {"result" : post})

def post(request):
    contents = Post.objects.all()
    return render(request, 'post.html', {'post_list' : contents})

def create(request):
    post = Post()
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.pub_date = timezone.datetime.now()
    post.mbti = request.GET['mbti']
    post.save()
    return redirect('post')

def new (request):
    return render(request, 'new.html')

def enfp(request):
    return render(request, 'enfp.html')

def isfj(request):
    return render(request, 'isfj.html')


def infp(request):
    return render(request, 'infp.html')

def whoami(req):
    if req.method == "GET":
        mymbti = req.GET['mbti']
        if mymbti == '2':
            return render(req,'isfj.html')
        elif mymbti == '7':
            return render(req,'infp.html')
        elif mymbti == '11':
            return render(req,'Enfp.html')
        elif mymbti == '13':
            return render(req,'estj.html')