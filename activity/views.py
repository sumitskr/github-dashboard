from django.http import HttpResponse
from .forms import Registration,Login
from django.shortcuts import render
from .models import Git_user
from datetime import date,datetime,timedelta
from .dashboard import sumit_repl
def index(request):
    return render(request,"index.html")

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
            if not Git_user.objects.filter(username=username):
                ins = Git_user(name=name,email=email,username=username,password=password,token=token,date=str(date.today()))
                ins.save()
            else:
                return HttpResponse("user not  available")
    context = {'registration_form':registration_form}
    return render(request,'registration.html',context)


def login(request):
    login_form = Login()
    if request.method == 'POST':
        login_form = Login(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
    context = {'login_form':login_form}
    return render(request,'login.html',context)

def activity(request):
    obj = sumit_repl()
    set_interval = 60
    t=Git_user.objects.filter(username="sumitskr")[0]
    date_range ={'min':datetime.today().strftime("%Y,%m,%d"),"max":(datetime.today()-timedelta(days=set_interval)).strftime("%Y,%m,%d")}
    obj.set_token(t.token)
    obj.initiate()
    obj.repo_list()
    obj.set_date(set_interval)
    obj.activity_count()
    data = obj.get_data()
    context ={'data':data,'date_range':date_range}
    return render(request,"activity.html",context)

