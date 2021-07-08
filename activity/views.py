from django.http import HttpResponse, request
from django.shortcuts import redirect, render
from datetime import date
from .dashboard import sumit_repl
from .forms import UserFrom,Git

def index(request):
    return HttpResponse("hello")
def registration(request):
    userform = UserFrom()
    gitform = Git()
    # if request.method == 'POST':
    context = {'userform':userform,'gitform':gitform}
    return render(request,'registration.html',context)
        




def dashboard(request):

    return render(request,'dashboard.html')
