from django.db.models.fields import EmailField
from django.forms import forms
from django.forms.fields import CharField
from django.forms.widgets import PasswordInput

class Registration(forms.Form):
    name = CharField(max_length=40,min_length=5,required=True)
    email = CharField(max_length=30,required=True)
    username = CharField(min_length=8,max_length=20,required=True)
    password = CharField(max_length=30, widget=PasswordInput,required=True)
    token = CharField(max_length=40,min_length=40,required=True)