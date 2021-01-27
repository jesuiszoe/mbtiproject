from django.shortcuts import render
from django.http.response import HttpResponse


def home(req):
    return render(req,"home.html")

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
