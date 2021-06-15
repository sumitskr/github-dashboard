from django.db import models
from django.db.models.fields import Field 


class Git_users(models.Model):
    id = models.AutoField(primary_key=True) 
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20)
    git_token = models.CharField(max_length=40)
    registration_date = models.DateField()