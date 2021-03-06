from django.shortcuts import render
from django.http import HttpResponse
from .forms import VacationtripForm
from django.contrib import messages

# Create your views here.

def home(request):
    form = VacationtripForm()
    if request.method=='POST':
        form = VacationtripForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Object Saved Successfully")
            form = VacationtripForm()
    # context = {'form' : form}
    # return render(request, 'vacation/home.html', context)
    return render(request, 'vacation/home.html', locals())