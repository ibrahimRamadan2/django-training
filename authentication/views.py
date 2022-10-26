from rest_framework import status
from rest_framework.views import APIView
from users.serializers import User_Data_Serializer
from users.models import Extended_User 
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from .serializers import Login_serializer
from rest_framework.response import Response
 
from knox.models import AuthToken
from django.contrib.auth import authenticate, login
# Create your views here.


class LoginView(APIView):
    authentication_classes = [BasicAuthentication,] 

    def post(self,  request):
        serializer = Login_serializer(data =request.data)
        if(serializer.is_valid()):
            user = authenticate(request , username=request.data['username'] , password=request.data['password'])
            if(user is not None):
                token =AuthToken.objects.create(user)[1]
                cur_user = Extended_User.objects.get(username = request.data['username'] )
                cur_serializer = User_Data_Serializer(cur_user)
                login (request , cur_user)
                return Response({
                    'token':token  , 
                    'user':  cur_serializer.data  ,  
                     
                }) 
            return Response(serializer.errors  , status.HTTP_400_BAD_REQUEST)
         
        return Response( serializer.errors, status.HTTP_400_BAD_REQUEST)
 
class Create_User(APIView):
    def get(self , request):
        pass


    def post(self , request):
        print(request.data)
        Response(status.HTTP_200_OK)
# 




