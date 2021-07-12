from django.db import models

# Create your models here.

# //////////////////  Many To Many Relationship Example ////////////////
# A model Book has many-to-many relationship with a model Author, i.e. an book can be written by multiple authors and an author can write multiple books.
# Many-to-many relations are defined using ManyToManyField field of django.db.models.
class Author(models.Model):
	name = models.CharField(max_length = 100)
	desc = models.TextField(max_length = 300)
	
	def __str__(self):
		return str(self.name)

class Book(models.Model):
	title = models.CharField(max_length = 100)
	desc = models.TextField(max_length = 300)
	authors = models.ManyToManyField(Author)
