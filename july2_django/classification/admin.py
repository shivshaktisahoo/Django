from django.contrib import admin
from .models import Garmnentscolmn
# Register your models here.

class GarmnentscolmnAdmin(admin.ModelAdmin):
    list_display = ('id', 'day', 'team', 'targeted_productivity','idle_men', 'no_of_workers')
    list_filter = ('day',) 


admin.site.register(Garmnentscolmn, GarmnentscolmnAdmin)