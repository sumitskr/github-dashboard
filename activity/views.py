from django.http import HttpResponse, response
from rest_framework import serializers
from .forms import Registration
from django.shortcuts import render
from .models import Git_user
from datetime import date
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import Userserializers,Userdetails,Userinsertion
from activity import serializer


@api_view(['GET','POST'])
def index(request):
    api_urls={
        'users':'/users_list/',
        'user_detail':'/user_detail/<str:username>',
        'user_update':'/user_update',
        

    }
    return Response(api_urls)

@api_view(["GET"])
def user_list(request):
    data = Git_user.objects.all()
    serializer = Userserializers(data,many=True)
    return Response(serializer.data)
@api_view(["GET"])
def user_detail(request,username):
    data = Git_user.objects.get(username=username)
    serializer = Userdetails(data,many=False)
    return Response(serializer.data)
@api_view(['POST'])
def user_update(request):
    serializer = Userinsertion(data=request.data)
    if serializer.is_valid():
        print(serializer.data)
    return Response(serializer.data)







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
            if not Git_user.objects.filter():
                ins = Git_user(name=name,email=email,username=username,password=password,token=token,date=str(date.today()))
                ins.save()
            else:
                return HttpResponse("user not  available")
    context = {'registration_form':registration_form}
    return render(request,'registration.html',context)

# @api_view(["GET","POST"])
# def apioverview(request):

