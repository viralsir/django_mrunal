from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1 style="color:blue;text-align:center">hello</h1>');

def about(request):
    return HttpResponse('<h1 style="color:blue;text-align:center">about page</h1>')

def greetings(request,username):
    return HttpResponse(f'<h1 style="color:blue;text-align:center">hello {username} </h1>')