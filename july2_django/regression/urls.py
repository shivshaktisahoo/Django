from django.urls import path
from .views import *

urlpatterns = [
            path('', regre, name='regre'),
            path('output/', output, name='output'),
]