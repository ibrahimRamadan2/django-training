 
import imp
from tkinter.tix import InputOnly
from django.db import models
import datetime
# Create your models here.

class ArtistQuerySet(models.QuerySet):
    def getAcceptedCount(self, itemSet):
        c=0  
        for i in itemSet : 
            c+=(i.isAccepted == True)
        return c
    
    def order_by(self , filterName="stageName") :
        if(filterName == "approved_albums"):
            artists = self.all()
            lst = []
            for artist in artists:
                cnt = self.getAcceptedCount(artist.album_set.all())
                lst.append([artist , cnt])
            for i in range(len(lst)):
                for x in range(i+1, len(lst)):
                    if(lst[i][1] < lst[x][1]):
                        temp = lst[i] 
                        lst[i] = lst[x] 
                        lst[x] =temp 
            result=[]
            for i in lst:
                result.append(i[0])        
            return result 

        else :
            return super().order_by(filterName)

class ArtistManger(models.Manager):
    def get_queryset(self) :
        return ArtistQuerySet(self.model , using=self._db)
        

class Artist(models.Model):
    stageName = models.CharField( max_length=60 , unique=True)
    SocialLink = models.URLField(max_length=300 , blank=True)
    objects = ArtistManger()
    def __str__(self) -> str:
        return f"{self.stageName}"
    class Meta : 
        ordering = ('stageName',)
        
 