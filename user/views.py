from django.shortcuts import render
from django.http.response import HttpResponse


def first(req):
    return render(req,"first.html")

def register(req):
    return render(req,"register.html")

def board(req):
    if req.method == "GET":
        mbti = req.GET['mbti']
        title = req.GET['title']
        body_text = req.GET['body_text']
        

        data = {'mbti':mbti, 'title':title, 'body_text':body_text}
        return render(req,"board.html",data)
    return render(req,"board.html")


# Create your views here.
