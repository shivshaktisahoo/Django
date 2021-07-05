from django.contrib import admin
from .models import Realestatecolmn
# Register your models here.

class RealestatecolmnAdmin(admin.ModelAdmin):
    list_display = ('id', 'house_age', 'MRT_station', 'con_stores','latitude', 'longitude','predicted')
    list_filter = ('con_stores',) 


admin.site.register(Realestatecolmn, RealestatecolmnAdmin)