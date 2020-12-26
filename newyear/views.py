from django.shortcuts import render
from datetime import datetime
# Create your views here.
def home(request):
    now=datetime.now()
    return render(request,"newyear/home.html",{
        "newyear": now.month==1 and now.day==1
    })