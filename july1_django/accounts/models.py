from django.db import models

# Create your models here.
gender_list=[('male','male'),('female','female')]
class Person(models.Model):
    first_name = models.CharField(max_length=50,default="")
    last_name = models.CharField(max_length=50,default="")
    age = models.IntegerField(default=18)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    desc = models.TextField()
    salary = models.FloatField()
    gender = models.CharField(choices=gender_list,max_length=10,default="male")
    is_verify = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.id} | {self.first_name} {self.last_name} | {self.gender} | {self.age} | {self.email} | {self.is_verify}"

class Student(models.Model):
    first_name = models.CharField(max_length=50,default="")
    last_name = models.CharField(max_length=50,default="")
    age = models.IntegerField(default=18)
    Student_class = models.IntegerField(default=1)
    rollno = models.IntegerField(null=True, blank=True)
    is_verify = models.BooleanField(default=False)

carrer_choice = [
    ('Programmer', 'Programmer'),
    ('Teacher', 'Teacher'),
    ('Businessman', 'Businessman'),
    ('Farmer', 'Farmer'),
    ('Doctor', 'Doctor')]

class Carrer(models.Model):
    carrer = models.CharField(choices=carrer_choice, max_length=20, default='Businessman')
    first_name = models.CharField(max_length=50,default="")
    last_name = models.CharField(max_length=50,default="")
    age = models.IntegerField(default=18)
    address = models.CharField(max_length=50,default="")