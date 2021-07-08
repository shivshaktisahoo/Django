from django.contrib import admin

# Register your models here.
from .models import Vacationtrip
# Register your models here.

class VacationtripAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age','country', 'contactno','package','no_of_days')
    list_filter = ('country',) 


admin.site.register(Vacationtrip, VacationtripAdmin)