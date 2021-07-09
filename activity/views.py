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
    if request.method == 'POST':
        userform = UserFrom(data=request.POST)
        gitform = Git(data=request.POST)
        # print(gitform)
        if userform.is_valid() and gitform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()
            git_data = gitform.save(commit=False)
            git_data.username = user
            git_data.save()
        
    context = {'userform':userform,'gitform':gitform}
    return render(request,'registration.html',context)
        




def dashboard(request):

    return render(request,'dashboard.html')
