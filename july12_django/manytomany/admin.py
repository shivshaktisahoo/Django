from django.contrib import admin
from .models import *

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc')
    list_filter = ('name',) 

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')
    list_filter = ('authors',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)