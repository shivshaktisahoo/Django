from django.db import models

# Create your models here.
day_list=[
    ('1','Saturday'),
    ('2','Sunday'),
    ('3','Monday'),
    ('4','Tuesday'),
    ('5','Wednesday'),
    ('6','Thursday')]
pred_list = [('Medium productivity','Medium productivity'),
        ('High productivity','High productivity')]
class Garmnentscolmn(models.Model): 
    username = models.CharField(max_length=40)
    day = models.CharField(choices=day_list,max_length=20,default="Saturday")
    team = models.IntegerField(default=0)
    targeted_productivity = models.FloatField(default=0)
    over_time = models.IntegerField(default=0)
    incentive = models.IntegerField(null=True, blank=True)
    idle_time = models.IntegerField(unique=True)
    idle_men = models.IntegerField(default=0)
    no_of_style_change = models.IntegerField(default=0)
    no_of_workers = models.IntegerField(default=0)
    predicted = models.CharField(choices=pred_list, max_length=40)
    
