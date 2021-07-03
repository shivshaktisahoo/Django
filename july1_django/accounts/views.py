from django.shortcuts import render
from .models import Person, Student, Carrer
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("<h1>Welcome to Home page of Accounts</h1>")

def person(request):
    try:
        data = request.GET['status']
        print(data)
        persons = Person.objects.filter(is_verify=data)
    except:
        persons = Person.objects.all()
        print("hai")
    context = {'persons':persons}
    return render(request, 'persons.html', context)

def student(request):
    try:
        data = request.GET['st_class']
        # print(data)
        students = Student.objects.filter(Student_class=data)
        print(students)
    except:
        students = Student.objects.all()
    context = {'students':students}
    return render(request, 'students.html', context)

def carrer(request):
    try:
        data = request.GET['carrer_choice']
        print(data)
        if data == 'All':
           carrers = Carrer.objects.all()
        else: 
            carrers = Carrer.objects.filter(carrer=data)
    except:
        carrers = Carrer.objects.all()
    list1 = ['Doctor', 'Businessman', 'Farmer', 'Programmer', 'Teacher']
    context = {'carrers':carrers, 'list1': list1}
    return render(request, 'carrers.html', context)