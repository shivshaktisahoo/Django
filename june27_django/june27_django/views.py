from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    try:
        data = request.GET
        name = data['name']
        print(data)
        data1 = dict(data)
        data1.pop('name')
        marks = [(i,int(data1[i][0])) for i in data1]
   
        print(marks)
        total = 0
        for i in data1.values():
            total = total + int(i[0]) 
        percentage = (total/400)*100
        if percentage>=75.0:
            division = "1st"
        elif percentage>=50.0:
            division = "2nd"
        elif percentage>=35.0:
            division = "3rd"
        else:
            division = "Fail"
        context = {'name':name, "total":total, "per":percentage,'division':division,"marks": marks}
        print(f'total is {total} and percentage is {percentage} %')
    
        return render(request, 'output.html', context)
    except:
        pass

    return render(request, 'home.html')


def about(request):
    print("about is called")
    return render(request, 'home.html')




