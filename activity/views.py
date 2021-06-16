from django.http import HttpResponse
from .forms import Registration
from django.shortcuts import render

def index(request):
    return HttpResponse("hello")

def registration(request):
    registration_form = Registration()
    context = {'registration_form':registration_form}
    return render(request,'registration.html',context)