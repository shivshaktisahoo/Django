from django.contrib import admin
from .models import *

# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artist')
    list_filter = ('artist',) 

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'album')
    list_filter = ('album',)

admin.site.register(Album,AlbumAdmin)
admin.site.register(Song,SongAdmin)