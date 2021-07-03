from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('person/', person, name='person'),
    path('student/', student, name='student'),
    path('carrer/', carrer, name='carrer'),
]