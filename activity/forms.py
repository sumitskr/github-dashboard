from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from .models import Git
from django.utils.translation import ugettext_lazy as _
class UserFrom(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name','last_name','username','password','email',)
        help_texts = {
            'username':"",

            
        }
#form that connects the userform
class Git(forms.ModelForm):
    class Meta():
        model = Git
        fields = ('Personal_Access_Token','contact')

