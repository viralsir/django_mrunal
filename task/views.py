from django.shortcuts import render,redirect

tasks=["check email","check balance","repair cycle"]

# Create your views here.
def home(request):
    return render(request,"task/home.html",{
        "tasks":tasks
    })

def add_task(request):
    if request.method == 'POST':
        tasks.append(request.POST["task"])
        return redirect('task-home')
    return render(request,"task/addtask.html")