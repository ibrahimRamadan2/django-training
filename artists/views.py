from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.views import View
from artists.models import Artist
from .forms import ArtistForm 
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import  status
from .serializers import Artist_Serializer
# Create your views here.

class indexView(APIView):
    def get(self,request):
        artists = Artist.objects.all() 
        serializer = Artist_Serializer(artists , many =True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = Artist_Serializer(data=request.data)
        print(request.data)
        if(serializer.is_valid()):
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class createView(View):
    def get(self, request) :
        form =ArtistForm()
        return render(request , "artists/create.html" , {'form':form})

    def post(self, request):
        form = ArtistForm(request.POST)
        if(form.is_valid()):
            name = request.POST['stage_name']
            form.save()
            return HttpResponseRedirect("/artist")
        return render(request , "/create.html" , {'form':form})
