from dataclasses import field
import email
from rest_framework import serializers
from .models import Extended_User


class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Extended_User
        fields=['username','email','password',]
    
    def create(self, validated_data):
        user = Extended_User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user 
    def validate(self, data) :
        password = data['password']
        num_cnt  , symbol_cnt , char_cnt=0,0,0
         
        for ch in password :
            if(ch >='A' and ch <='z'):
                char_cnt+=1 
            if(ch>='0' and ch <= '9'):
                num_cnt+=1 
            else :
                symbol_cnt+=1
        if(num_cnt==0 or symbol_cnt==0 or char_cnt==0 or len(password) <8):
            raise serializers.ValidationError(f"password should have chars and numbers and symbols and at least 8 chars")
        return data
    
class User_Data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Extended_User
        fields=['id','username','email','bio',]
        