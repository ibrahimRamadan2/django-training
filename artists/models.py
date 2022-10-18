 
import imp
from tkinter.tix import InputOnly
from django.db import models
import datetime
# Create your models here.

class ArtistQuerySet(models.QuerySet):
     
    def order_by(self , filterName="stageName") :
        if(filterName == "approved_albums"):
            # sort artists with thier album_cnt in  dec order
            f = models.Q(album__isAccepted =True)
            return Artist.objects.all().annotate(cnt = models.Count('album',f)).order_by('-cnt')
        else :
            return super().order_by(filterName)

class ArtistManger(models.Manager):
    def get_queryset(self) :
        return ArtistQuerySet(self.model , using=self._db)
        

class Artist(models.Model):
    stageName = models.CharField( max_length=60 , unique=True)
    SocialLink = models.EmailField(max_length=254 , blank=True)
    objects = ArtistManger()
    def __str__(self) -> str:
        return f"{self.stageName}"
    class Meta : 
        ordering = ('stageName',)
        
 