from django.urls import path
from .views import *

urlpatterns = [
    path('', manager, name='manager'),
    path('managerlist', managerlist, name='managerlist'),
    path('edit/<int:id>/', edit_manager, name='edit_manager'),
    path('profile/<int:id>/', profile, name='profile'),
    path('delete/<int:id>/', delete, name='delete'),
    path('room/', room, name='room'),

]