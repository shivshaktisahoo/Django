from django.db import models

# Create your models here.

# //////////////////  Many To One Relationship Example ////////////////
# A model Song has many-to-one relationship with a model Album, i.e. an album can have many songs, but one song cannot be part of multiple albums.
# Many-to-one relations are defined using ForeignKey field of django.db.models.
class Album(models.Model):
	title = models.CharField(max_length = 100)
	artist = models.CharField(max_length = 100)
	
	def __str__(self):
		return str(self.artist)

class Song(models.Model):
	title = models.CharField(max_length = 100)
	album = models.ForeignKey(Album, on_delete = models.CASCADE)

