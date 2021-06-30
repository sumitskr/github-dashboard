from django.http import HttpResponse, response
from rest_framework.exceptions import ValidationError
from .forms import Registration
from django.shortcuts import render
from .models import Git_user,Contact
from datetime import date, datetime
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from .serializer import Issueserializer, Userserializers,Userdetails,Userinsertion,Contactcreate
from activity import serializer
from rest_framework import status
from .dashboard import sumit_repl
import json
from datetime import datetime,timedelta

@api_view(['GET'])
def index(request):
    api_urls={
        'users':'https://sumitapi2.herokuapp.com//user_list/' ,
        'user_detail':'https://sumitapi2.herokuapp.com/user_detail/<str:username>',
        'user_insertion':'https://sumitapi2.herokuapp.com/user_insertion/',
        'issues':'https://sumitapi2.herokuapp.com/issues/',
        'contact':'https://sumitapi2.herokuapp.com/contact/' ,  #issue = contact
        'dataset':'https://sumitapi2.herokuapp.com/dataset/<str:username>',
        

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
def user_insertion(request):
    serializer = Userinsertion(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.validated_data
        serializer.save(date=datetime.now()) #https://simpleisbetterthancomplex.com/tutorial/2019/04/07/how-to-save-extra-data-to-a-django-rest-framework-serializer.html
        return Response(serializer.data,status=status.HTTP_201_CREATED)
@api_view(['GET'])
def issues(request):
    data = Contact.objects.all()
    serializer = Issueserializer(data,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def contact(request):
    serializer = Contactcreate(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.validated_data
        serializer.save(date=datetime.now())
        return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET'])
def dataset(request,username):
    try :
        t=Git_user.objects.get(username=username)
        print(t)
    except Git_user.DoesNotExist:
        t=None
    if t!= None:
        obj = sumit_repl()
        set_interval = 60
        date_range ={'min':datetime.today().strftime("%Y,%m,%d"),"max":(datetime.today()-timedelta(days=set_interval)).strftime("%Y,%m,%d")}
        obj.set_token(t.token)
        obj.initiate()
        obj.repo_list()
        obj.set_date(set_interval)
        obj.activity_count()
        data = obj.get_data()
        print("data",data)
        jsonStr = json.dumps(data)
        json_data = {'data':jsonStr}
        var = status.HTTP_200_OK
    else:
        jsonStr = "Sorry No daata Found"
        json_data = {'data':jsonStr}
        var = status.HTTP_204_NO_CONTENT
    return Response(json_data,status=var)







