from django.http import HttpResponse
from .forms import Registration
from django.shortcuts import render
from .models import Git_user
from datetime import date
def index(request):
    return HttpResponse("hello")

def registration(request):
    registration_form = Registration()
    if request.method == "POST":
        registration_form=Registration(request.POST)
        if registration_form.is_valid():
            name = registration_form.cleaned_data['name']
            email = registration_form.cleaned_data['email']
            username = registration_form.cleaned_data['username']
            password = registration_form.cleaned_data['password']
            token = registration_form.cleaned_data['token']
            # print(name,username)
            ins = Git_user(name=name,email=email,username=username,password=password,token=token,date=str(date.today()))
            ins.save()
    context = {'registration_form':registration_form}
    return render(request,'registration.html',context)