from django.db.models import fields
from rest_framework import serializers
from .models import Git_user
class Userserializers(serializers.ModelSerializer):
    class Meta:
        model = Git_user
        fields = ('username','email','date')
class Userdetails(serializers.ModelSerializer):
    class Meta:
        model = Git_user
        fields = '__all__'
class Userinsertion(serializers.ModelSerializer):
    class Meta:
        model = Git_user
        fields = '__all__'