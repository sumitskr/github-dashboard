from django.http import HttpResponse
from django.shortcuts import render

from .forms import Git_user_form
def index(request):
    return render(request,'index.html')
def register(request):
    registration = Git_user_form()
    return render(request,'registration.html',{'registration':registration})