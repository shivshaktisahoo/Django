from django.urls import path
from .views import *
urlpatterns = [
    path('', classify, name='classify'),
    path('history/', history, name="history"),
] 