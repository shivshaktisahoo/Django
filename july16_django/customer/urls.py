from django.urls import path
from .views import *
app_name = 'customer'

urlpatterns = [
    path('', customer, name='customer'),
    path('customerlist', customerlist, name='customerlist'),
    path('edit/<int:id>/', edit_customer, name='edit_customer'),
    path('profile/<int:id>/', profile, name='profile'),
    path('delete/<int:id>/', delete, name='delete'),
]