from django.shortcuts import render

# Create your views here.

def index (request):
    return render (request, 'main/')

def Change(request):
    return render (request, )