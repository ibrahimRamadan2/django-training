from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.views import View
from artists.models import Artist
from .forms import ArtistForm
# Create your views here.

class indexView(View):
    artists = Artist.objects.all() 
    def get(self,request):
        return render(request , "artists/index.html" , {'artists':self.artists})
    
    def post(self,request):
        return render(request , "artists/index.html" , {'artists':self.artists})

class createView(View):
    def get(self, request) :
        form =ArtistForm()
        return render(request , "artists/create.html" , {'form':form})

    def post(self, request):
        form = ArtistForm(request.POST)
        if(form.is_valid()):
            name = request.POST['stageName']
            form.save()
            return HttpResponseRedirect("/artist")
        return render(request , "/create.html" , {'form':form})
