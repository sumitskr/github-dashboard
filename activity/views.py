from django.http import HttpResponse
from .forms import Registration
from django.shortcuts import render

def index(request):
    return HttpResponse("hello")

def registration(request):
    registration_form = Registration()
    if request.method == "POST":
        registration_form=Registration(request.POST)
        if registration_form.is_valid():
            name ="sumit"
    context = {'registration_form':registration_form}
    return render(request,'registration.html',context)