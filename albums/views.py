import http
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import albumForm
from .models import Album


def index(request):
    all = Album.objects.all()

    return render(request, "albums/index.html", {
        'albums': all,
        'cnt': len(all),
    })


def create(request):
    form = albumForm()

    if (request.method == 'GET'):
        return render(request, "albums/create.html", {'form': form})
    else:
        form = albumForm(request.POST)
        print(request.POST['name'])
        if (form.is_valid()):
            form.save()
            return HttpResponseRedirect("/album")
        return render(request, "albums/create.html", {'form': form})
