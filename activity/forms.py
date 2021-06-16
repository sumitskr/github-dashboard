from django.db.models.fields import EmailField
from django.forms import forms
from django.forms.fields import CharField
from django.forms.widgets import PasswordInput

class Registration(forms.Form):
    name = CharField(max_length=40,min_length=5)
    email = EmailField(max_length=30)
    password = CharField(max_length=32, widget=PasswordInput)
    token = CharField(max_length=40,min_length=40,required=True)