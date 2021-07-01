from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('person/<str:verify>/', person, name='person'),
    path('student/<int:student_class>/', student, name='student'),
    path('carrer/<str:carrer_name>/', carrer, name='carrer'),
]