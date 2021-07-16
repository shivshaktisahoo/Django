from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignupForm
from django.contrib import messages

# Create your views here.

def create(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "User Saved Successfully")
            return render(request, 'main/continue.html')
        else:
            messages.error(request, "Please Provide valid data")

    return render(request, 'main/createuser.html', locals())
