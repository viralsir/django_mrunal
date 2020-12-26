from django.shortcuts import render

tasks=["check email","check balance","repair cycle"]

# Create your views here.
def home(request):
    return render(request,"task/home.html",{
        "tasks":tasks
    })

def add_task(request):
    return render(request,"task/addtask.html")