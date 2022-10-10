from multiprocessing import managers
from django.db import models
from artists.models import Artist
# Create your models here.

class AlbumManager(models.Manager):
    def getCount(self):
        return self.filter(cost__gte=50.0)
    

class Album(models.Model):
    name = models.CharField(max_length=100 , default="New Album" , blank=True)
    creationDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    releaseDate = models.DateTimeField(auto_now=False, auto_now_add=False, db_index=True)
    cost = models.FloatField()
    artist = models.ForeignKey(Artist , on_delete=models.CASCADE)
    objects=AlbumManager()
    
    def __str__(self) -> str:
        return  f"{self.name} , {self.cost}"
 
 
from albums.models import Album ,Artist 
x=Album.objects.con
for item in x :
    print(item)