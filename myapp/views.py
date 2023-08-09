from django.shortcuts import render
from django.http import HttpResponse

def hello( request ):
    return HttpResponse('Hello world!')

def about( request ):
    return HttpResponse('<h1>About us</h1>')
