from django.shortcuts import render
from .models import Contactinfo

# Create your views here.

# This view.py is for main-site which will control all other application
# for this view.py, we will define urls in main root urls.py and will not going create urls.py in core app
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    try:
        data = request.GET
        Contactinfo.objects.create(firstname=data['firstname'],
        lastname=data['lastname'],description=data['description'])
        return render(request, 'core/home.html')
    except:
        return render(request, 'core/contact.html')
