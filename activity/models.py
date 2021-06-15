from django.db import models
from django.db.models.fields import Field 


class Users(models.Model):
    user_id = models.AutoField
    username = models.CharField(max_length=20,unique=True)
    git_token = models.CharField(min_length=40,max_length=40)
    registration_date = models.DateField()