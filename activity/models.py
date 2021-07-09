from django.db import models
from django.db.models.fields import AutoField, CharField, DateField, EmailField
from django.contrib.auth.models import User
from django.core import validators
class Git(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    Personal_Access_Token = models.CharField(max_length=40,null=False,validators=[validators.MinLengthValidator(40)])
    contact = models.CharField(max_length=10,null=False)
    def __str__(self) -> str:
        return self.username.username

