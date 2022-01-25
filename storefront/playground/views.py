from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse ## Import by Hamed to handle responses

# Create your views here.
# This module acting like request handler

## Simple fucntion to handle and response message
def say_hello(request):
    return HttpResponse('Hello from django')

## func to return HTML 
def say_hello_HTML(request):
    return render(request,'hello.html' ,{ 'name' : 'hamed' })
