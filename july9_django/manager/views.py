from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ManagerForm
from .models import Manager, Room
from django.contrib import messages

# Create your views here.
def manager(request):
    manager_list = Manager.objects.all()
    form = ManagerForm()
    if request.method=='POST':
        form = ManagerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"CONFIRMED !!!!")
            return redirect('managerlist')
    return render(request, 'manager/manager.html', locals())

def managerlist(request):
    manager_list = Manager.objects.all()
    return render(request, 'manager/managerlist.html',locals())

def edit_manager(request, id):
    object_ = Manager.objects.filter(id=id).first()
    form = ManagerForm(instance=object_)
    if request.method == 'POST':
        form = ManagerForm(request.POST, request.FILES,
                          instance=object_)
        if form.is_valid():
            form.save()
            messages.success(request, "Object Updated Successfully")
            return redirect('managerlist')
        else:
            messages.error(request, "Please Provide valid data")

    return render(request, 'manager/manager.html', locals())


def profile(request, id):
    mg = Manager.objects.filter(id=id).first()
    return render(request, 'manager/profile.html', locals())


def delete(request, id):
    Manager.objects.filter(id=id).first().delete()
    return redirect('managerlist')

def room(request):
    room_list = Room.objects.all()
    return render(request, 'room.html',locals())