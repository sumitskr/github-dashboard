from typing import Hashable
from django.db import models
from django.db.models.fields import AutoField, CharField, DateField, EmailField


class Git_user(models.Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=40)
    username = CharField(max_length=20,default="")
    email = EmailField(max_length=30)
    password = CharField(max_length=20)
    token = CharField(max_length=40)
    date = DateField(null=True)

