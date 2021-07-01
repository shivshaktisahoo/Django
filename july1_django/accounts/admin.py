from django.contrib import admin
from .models import Person, Student, Carrer
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age', 'email')
    list_filter = ('is_verify',) 

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'Student_class', 'rollno')
    list_filter = ('Student_class',) 

class CarrerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age', 'carrer')
    list_filter = ('carrer',) 

admin.site.register(Person, PersonAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Carrer, CarrerAdmin)