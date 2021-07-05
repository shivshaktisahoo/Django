from django.shortcuts import render
from django.http import HttpResponse
from .models import Garmnentscolmn
import pickle
# Create your views here.

def classify(request):
    try:
        data = request.GET
        day1 = data['day'] # this is done only to generate error if data is empty 
        print(data)
        data1 = data.copy()
        data1.pop('user')
        list3 = [float(data1['targeted_productivity']) if i == 'targeted_productivity' else int(data1[i]) for i in data1.keys()]
        
        pickle_in = open('garments_model.pickle', 'rb')
        reg = pickle.load(pickle_in)
        result = reg.predict([list3])
        if result[0]==1.0:
            res = 'High productivity'
        else:
            res = 'Medium productivity'

        Garmnentscolmn.objects.create(username = data['user'],
        day = day1,
        team = int(data['team']),
        targeted_productivity = float(data['targeted_productivity']),
        over_time = int(data['over_time']),
        incentive = int(data['incentive']),
        idle_time = int(data['idle_time']),
        idle_men = int(data['idle_men']),
        no_of_style_change = int(data['no_of_style_change']),
        no_of_workers = int(data['no_of_workers']),
        predicted = res)

        g1 = Garmnentscolmn.objects.all()
        list1 = []
        for i in g1: 
            list1.append(i.username)
        list1 = list(set(list1))
        print(list1)
        
        context = {'user_name':data['user'],'list1': list1}

        return render(request, 'classification/history.html', context)
    except Exception as e:
        print(e)
    return render(request, 'classification/classifyhome.html')


def history(request):
    try:
        data = request.GET['user']
        print(data)
        if data=='All':
            g_table = Garmnentscolmn.objects.all()
        else:
            g_table = Garmnentscolmn.objects.filter(username=data)
    except:
        g_table = Garmnentscolmn.objects.all()
    g1 = Garmnentscolmn.objects.all()
    list1 = []
    for i in g1: 
        list1.append(i.username)
    list1 = list(set(list1))
    print(list1)
    context = {'gc_table': g_table,'list1': list1}
    return render(request, 'classification/history.html', context)