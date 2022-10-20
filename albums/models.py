from datetime import datetime
from django.db import models
from artists.models import Artist
from model_utils.models import TimeStampedModel


# Create your models here.


class Album(TimeStampedModel):
    # now this model has 2 attrs from timeStamp model
    # 1 - created  (when this obj in created )
    # 2-  modified (when last save has done to this obj)
                                           
    name = models.CharField(blank=True, max_length=100, default="New Album")
    cost = models.FloatField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_at = models.DateTimeField(
        default=datetime.now(), auto_now=False, auto_now_add=False)
    isAccepted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        ordering = ('name',)


class song(models.Model):
    name=  models.CharField(max_length=100)
    image = models.ImageField(upload_to=None, height_field=100, width_field=100)
    
# from albums.models import Artist , Album
# Artist.objects.order_by("approved_albums")
# f = models.Q(album__isAccepted =True)
# x= Artist.objects.all().annotate(cnt = models.Count('album',f)).order_by('-cnt')
# x= Album.objects.all()[0].artist.stageName
