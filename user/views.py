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
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = {}
        if not ( username and password ):
            data['error'] = '모든 값을 입력해주세요.'
            return render(request, 'login.html', data)
        else:
            user = User.objects.get(username=username)
            if user.password == password:
                return redirect('home')
            else:
                data['error'] = '아이디 또는 비밀번호가 틀립니다.'
                return render(request, 'login.html', data)
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'detail.html', {"result" : post})

def show_post(request):
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



def whoami(req):
    if req.method == "GET":
        mymbti = req.GET['mbti']
        if mymbti == '2':
            return render(req,'isfj.html')
    
    
    