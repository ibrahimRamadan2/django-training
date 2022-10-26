from rest_framework import serializers
from users.models import Extended_User
from django.contrib.auth import authenticate, login
class Login_serializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    

     