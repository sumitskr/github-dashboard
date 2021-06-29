from django.db.models import fields
from rest_framework import serializers
from .models import Git_user,Contact
class Userserializers(serializers.ModelSerializer):
    class Meta:
        model = Git_user
        fields = ('username','email','date')
class Userdetails(serializers.ModelSerializer):
    class Meta:
        model = Git_user
        fields =  ('username','email','date')
        # fields = "__all__"
class Userinsertion(serializers.ModelSerializer):
    class Meta:
        model = Git_user
        fields = ('name','username','email','password','token')
class Issueserializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
class Contactcreate(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('name','email','issue_details')