from django.shortcuts import render
from django.http import HttpResponse
from .forms import VacationtripForm

# Create your views here.

def home(request):
    form = VacationtripForm()
    if request.method=='POST':
        form = VacationtripForm(request.POST)
        if form.is_valid():
            form.save()
            form = VacationtripForm()
    context = {'form' : form}
    return render(request, 'vacation/home.html', context)
