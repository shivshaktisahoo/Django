from django.shortcuts import render
from .models import Person, Student, Carrer
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("<h1>Welcome to Home page of Accounts</h1>")

def person(request, verify):
    # data = request.GET
    # print(data)
    # print(verify,type(verify))
    if verify == 'True':
        persons = Person.objects.filter(is_verify=True)
    elif verify == 'False':
        persons = Person.objects.filter(is_verify=False)
    else:
        persons = Person.objects.all()
    # print(persons)
    context = {'persons':persons}
    return render(request, 'persons.html', context)


def student(request, student_class):
    print(student_class,type(student_class))
    if (student_class == 0):
        students = Student.objects.all()
    else:
        students = Student.objects.filter(Student_class = student_class)
    context = {'students':students}
    return render(request, 'students.html', context)


def carrer(request, carrer_name):
    print(carrer_name,type(carrer_name))
    if (carrer_name == 'All'):
        carrers = Carrer.objects.all()
    else:
        carrers = Carrer.objects.filter(carrer = carrer_name)
    # carrers = Carrer.objects.all()
    context = {'carrers':carrers}
    return render(request, 'carrers.html', context)