from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    try:
        data = request.GET
        num = data['number']
        print(f'Number is {num}')

    except:
        pass

    return render(request, 'home.html')


def about(request):
    data = request.GET
    name = data['name']
    # science = data['mark1']
    # maths = data['mark2']
    # eng = data['mark3']
    # ssc = data['mark4']
    # total = int(science) + int(maths) + int(eng) + int(ssc)
    print(data)
    data1 = dict(data)
    data1.pop('name')
    total = 0
    for i in data1.values():
        total = total + int(i[0]) 
    
    print(f'total is {total} and percentage is {(total/400)*100} %')
    return HttpResponse(f'<h1 style="color:indigo; text-align: center; font-family: Verdana, Geneva, Tahoma, sans-serif;"><u> ABC SCHOOL </u></h1><hr><br><h2>Student Name : {name}</h2><p style="font-size: 150%;">Your Total marks : {total} / 400<br>Percentage : {(total/400)*100} %</p>')
    




