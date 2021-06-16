from django.http import HttpResponse
from .forms import Registration
from django.shortcuts import render

def index(request):
    return HttpResponse("hello")

def registration(request):
    return render(request,'registration.html')