from main.forms import TaskForm
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.

def index(request):
    tasks=Task.objects.order_by('title')[:5]
    return render(request, 'main/index.html', {'title': 'Main page', 'tasks' : tasks})

def about(request):
    return render(request,"main/about.html")

def create(request):
    error=""
    if request.method=="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error="Huina, peredelivai"

    form=TaskForm()
    context={'form':form , 'error' : error}
    return render (request,"main/create.html", context)