from django.shortcuts import render
from django.http import HttpResponse
import pickle
from .models import Realestatecolmn
# Create your views here.

def regre(request):
    try:
        data = request.GET
        age1 = data['house_age']  # this is intentionally done only to generate error if data is empty 
        print(data)
        data1 = data.copy()
        data1.pop('user')
        list3 = [int(data1[i]) for i in data1.keys()]
        print(f"list3= {list3}")
        pickle_in = open('real_estate.pickle', 'rb')
        reg = pickle.load(pickle_in)
        result = reg.predict([list3])
        print(f"result={result[0]}")

        Realestatecolmn.objects.create(username = data['user'],
        house_age = int(data['house_age']),
        MRT_station = int(data['MRT_station']),
        con_stores = float(data['con_stores']),
        latitude = int(data['latitude']),
        longitude = int(data['longitude']),
        predicted = abs(result[0]))
        
        g1 = Realestatecolmn.objects.all()
        list1 = []
        for i in g1: 
            list1.append(i.username)
        list1 = list(set(list1))
        # print(f"list1 = {list1}")
        context = {'user_name':data['user'],'list1': list1}
        return render(request, 'regression/regoutput.html', context)
    except Exception as e:
        print(f"error={e}")
    return render(request, 'regression/regrehome.html')


def output(request):
    try:
        data = request.GET['user']
        # print(data)
        if data=='All':
            g_table = Realestatecolmn.objects.all()
        else:
            g_table = Realestatecolmn.objects.filter(username=data)
    except:
        g_table = Realestatecolmn.objects.all()
    g1 = Realestatecolmn.objects.all()
    list1 = []
    for i in g1: 
        list1.append(i.username)
    list1 = list(set(list1))
    print(list1)
    context = {'gc_table': g_table,'list1': list1}
    return render(request, 'regression/regoutput.html', context)