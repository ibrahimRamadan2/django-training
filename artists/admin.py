from django.contrib import admin
from .models import Artist
from albums.models import Album
# Register your models here.

class AlbumInline(admin.StackedInline):
    model = Album

class ArtistAdmin(admin.ModelAdmin):
    list_display = ("stage_name", "accepted_albums",)
    
    def accepted_albums(self, obj):
        lst = obj.album_set.all()
        cnt = 0
        for album in lst:
            cnt += (album.isAccepted == True)
        return cnt 


admin.site.register(Artist, ArtistAdmin)
