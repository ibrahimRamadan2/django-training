from email.policy import default
from multiprocessing import managers
from django.db import models
from artists.models import Artist
# Create your models here.

    

class Album(models.Model):
    name = models.CharField(max_length=100 , default="New Album" , blank=True)
    creationDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    releaseDate = models.DateTimeField(auto_now=False, auto_now_add=False)
    cost = models.FloatField()
    artist = models.ForeignKey(Artist , on_delete=models.CASCADE)
    isAccepted = models.BooleanField(default=False)
    def __str__(self) -> str:
        return  f"{self.name}"
    class Meta:
        ordering = ('name',)
        
 
 