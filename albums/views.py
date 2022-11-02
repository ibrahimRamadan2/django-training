from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import albumForm
from .models import Album
from django.views import  View

class indexView(View):
    def get(self,request):
        all = Album.objects.all()
        return render(request, "albums/index.html", {
            'albums': all,
            'cnt': len(all),
        })

    def post(self):
        pass
 
class createView(View):
    def get(self,request):
        form = albumForm()
        return render(request, "albums/create.html", {'form': form})

    def post(self,request):
        form = albumForm(request.POST)
        print(request.POST['name'])
        if (form.is_valid()):
            form.save()
            return HttpResponseRedirect("/album")
        return render(request, "albums/create.html", {'form': form})

