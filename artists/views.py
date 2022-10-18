from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect

from artists.models import Artist
from .forms import ArtistForm
# Create your views here.

def index(request):
    artists = Artist.objects.all() 
    return render(request , "artists/index.html" , {'artists':artists})

def create(request):
    form =ArtistForm()
    if(request.method == 'GET'):
        return render(request , "artists/create.html" , {'form':form})
    # form = ArtistForm(request.POST)
    form = ArtistForm(request.POST)
    if(form.is_valid()):
        name = request.POST['stageName']
        form.save()
        return HttpResponseRedirect("/artist")
    return render(request , "/create.html" , {'form':form})
     