 
from re import search
import re
from django.shortcuts import render
from rest_framework.views import APIView
from django.db.models import Q 
from .models import Album
from .serializers import album_serializer 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from knox.auth import TokenAuthentication 
from rest_framework.permissions import    IsAuthenticatedOrReadOnly
from .filters import Album_List_Filter   
from artist.serializers import Artist_serializer
# Create your views here.


class  get_approved_albums(APIView):
    authentication_classes = [TokenAuthentication, BasicAuthentication, ]
    permission_classes = [ IsAuthenticatedOrReadOnly,]
    def get(self, request):
        query_list = Album.objects.filter(is_accepted = True)
        filter_list = Album_List_Filter(request.GET , queryset = query_list).qs
        result=[]
        for album in filter_list : 
            serializer =  album_serializer(album )
            result.append(serializer.data)
        return Response(result , status.HTTP_200_OK)

  
    def post(self, request):
         
        # check if the user is an artist or regular user 
        valid = request.user.artist_set.all().count()
        if(valid ==0):
            return Response({'error':"the user should be an artist"} , status.HTTP_403_FORBIDDEN)
        cnt  = Album.objects.filter(name = request.data['name']).count()
        if cnt > 0 :
            return Response({'error':"this album already exist"} , status.HTTP_406_NOT_ACCEPTABLE)
        
        artist_data = request.user.artist_set.all()[0] 
        serialzer = album_serializer(data=request.data)
        serialzer.is_valid(raise_exception=True)
        serialzer.create(serialzer.validated_data , artist_data)
        return Response(serialzer.data , status.HTTP_200_OK) 
             
             

# this is the same above view but filters are implemented manually ans asked in point 5 task 8
class get_approved_albums2(APIView):
    authentication_classes = [TokenAuthentication, BasicAuthentication, ]
    permission_classes = [ IsAuthenticatedOrReadOnly,]
    def get(self , request):
        params= request.GET
        
        min_cost , max_cost = 0.0 , float(1e9)
        contained_string = ''   # contained_string => /?name__icontains =blabla
        # return Response(params['cost'])
        if('name' in params):                
            contained_string = params.get('name')
        if('name__icontains' in params):
            contained_string = params.get('name__icontains') 
        # return Response(params)
        if('cost__lte' in params):
            max_cost = params.get('cost__lte') 
        if('cost__gte' in params):
            min_cost = params.get('cost__gte') 
        if('cost' in params):
            min_cost = params.get('cost') 
            max_cost = params.get('cost') 
        query_list = Album.objects.filter(Q(cost__gte= min_cost) & Q(cost__lte =max_cost) & 
        Q(name__icontains=contained_string) )
        result=[]
        for album in query_list : 
            serializer =  album_serializer(album )
            result.append(serializer.data)
        return Response(result , status.HTTP_200_OK)

    def post(self, request):
         
        # check if the user is an artist or regular user 
        valid = request.user.artist_set.all().count()
        if(valid ==0):
            return Response({" the user should be an artist "} , status.HTTP_403_FORBIDDEN)
        cnt  = Album.objects.filter(name = request.data['name']).count()
        if cnt > 0 :
            return Response({"this album already exist "} , status.HTTP_406_NOT_ACCEPTABLE)
        
        artist_data = request.user.artist_set.all()[0] 
        serialzer = album_serializer(data=request.data)
        serialzer.is_valid(raise_exception=True)
        serialzer.create(serialzer.validated_data , artist_data)
        return Response(serialzer.data , status.HTTP_200_OK) 