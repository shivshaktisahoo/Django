from django.urls import path
from .views import *

urlpatterns = [
    path('', customer, name='customer'),
    path('customerlist', customerlist, name='customerlist'),
    path('edit/<int:id>/', edit_customer, name='edit_customer'),
    path('profile/<int:id>/', profile, name='customer_profile'),
    path('delete/<int:id>/', delete, name='customer_delete'),
]