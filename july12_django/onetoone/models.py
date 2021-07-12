from django.db import models

# Create your models here.

# //////////////////  One To One Relationship Example ////////////////
# A model Car has one-to-one relationship with a model Vehicle, i.e. a car is a vehicle. 
# One-to-one relations are defined using OneToOneField field of django.db.models.
class Vehicle(models.Model):
	reg_no = models.IntegerField()
	owner = models.CharField(max_length = 100)

	def __str__(self):
		return str(self.reg_no)

class Car(models.Model):
	vehicle = models.OneToOneField(Vehicle, on_delete = models.CASCADE, primary_key = True)
	car_model = models.CharField(max_length = 100)