from django.shortcuts import render
from django.http.response import HttpResponse


def first(req):
    return render(req,"first.html")
# Create your views here.
