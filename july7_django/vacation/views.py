from django.shortcuts import render
from django.http import HttpResponse
from .forms import VacationtripForm
from django.contrib import messages
from .models import Vacationtrip

# Create your views here.

def home(request):
    form = VacationtripForm()
    if request.method=='POST':
        form = VacationtripForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"CONFIRMED !!!!")
            form = VacationtripForm()
    # context = {'form' : form}
    # return render(request, 'vacation/home.html', context)
    return render(request, 'home.html', locals())

def output(request):
    people = Vacationtrip.objects.all()
    return render(request,'output.html',locals())