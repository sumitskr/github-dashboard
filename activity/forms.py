from django.core.exceptions import ValidationError
from django.db.models.fields import EmailField
from django.forms import forms
from django.forms.fields import CharField
from django.forms.widgets import PasswordInput
from .models import Git_user

class Registration(forms.Form):
    name = CharField(max_length=40,min_length=5,required=True)
    email = CharField(max_length=30,required=True)
    username = CharField(min_length=8,max_length=20,required=True)
    password = CharField(max_length=30, widget=PasswordInput,required=True)
    token = CharField(max_length=40,min_length=40,required=True)

class Login(forms.Form):
    username = CharField(min_length=8,max_length=20) 
    password = CharField(max_length=30, widget=PasswordInput)
    def clean(self):
        cleaned_data = super().clean()
        # print(cleaned_data)
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        obj = Git_user.objects.filter(username=username)[0]
        if not Git_user.objects.filter(username=username):
            raise ValidationError("You are not registered")
        elif Git_user.objects.filter(username=username) and obj.password != password:
            raise ValidationError("Incorect password")
        return cleaned_data

    

