from django.contrib import admin
from .models import *
# Register your models here.
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'reg_no', 'owner')
    list_filter = ('reg_no',) 

class CarAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'car_model')
    list_filter = ('vehicle',)

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Car, CarAdmin)