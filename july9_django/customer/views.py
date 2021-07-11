from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomerForm
from .models import Customer
from django.contrib import messages

# Create your views here.
def customer(request):
    customer_list = Customer.objects.all()
    form = CustomerForm()
    if request.method=='POST':
        form = CustomerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"CONFIRMED !!!!")
            return redirect('customerlist')
    return render(request, 'customer/customer.html', locals())

def customerlist(request):
    customer_list = Customer.objects.all()
    return render(request, 'customer/customerlist.html',locals())

def edit_customer(request, id):
    object_ = Customer.objects.filter(id=id).first()
    form = CustomerForm(instance=object_)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES,
                          instance=object_)
        if form.is_valid():
            form.save()
            messages.success(request, "Object Updated Successfully")
            return redirect('customerlist')
        else:
            messages.error(request, "Please Provide valid data")

    return render(request, 'customer/customer.html', locals())


def profile(request, id):
    mg = Customer.objects.filter(id=id).first()
    return render(request, 'customer/profile.html', locals())


def delete(request, id):
    Customer.objects.filter(id=id).first().delete()
    return redirect('customerlist')
