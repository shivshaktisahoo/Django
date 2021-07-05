from django.shortcuts import render
from django.http import HttpResponse
import pickle
# Create your views here.

def classify(request):
    try:
        data = request.GET
        day1 = data['day'] # this is done only to generate error if data is empty 
        
        list3 = [float(data['targeted_productivity']) if i == 'targeted_productivity' else int(data[i]) for i in data.keys()]
        # print(list3)
        dict1 = {'1':'Saturday','2':'Sunday','3':'Monday','4':'Tuesday','5':'Wednesday','6':'Thursday'}
        if data['day'] in dict1.keys():
            day2 = dict1[data['day']]
        # Garmnentscolmn.objects.create(day=day2,
        # team = int(data['team']),
        # targeted_productivity = float(data['targeted_productivity']),
        # over_time = int(data['over_time']),
        # incentive = int(data['incentive']),
        # idle_time = int(data['idle_time']),
        # idle_men = int(data['idle_men']),
        # no_of_style_change = int(data['no_of_style_change']),
        # no_of_workers = int(data['no_of_workers']))

    
        # g1 = Garmnentscolmn(day='Sunday',
        # team = int(data['team']),
        # targeted_productivity = float(data['targeted_productivity']),
        # over_time = int(data['over_time']),
        # incentive = int(data['incentive']),
        # idle_time = int(data['idle_time']),
        # idle_men = int(data['idle_men']),
        # no_of_style_change = int(data['no_of_style_change']),
        # no_of_workers = int(data['no_of_workers']))
        # g1.save()

        pickle_in = open('garments_model.pickle', 'rb')
        reg = pickle.load(pickle_in)
        result = reg.predict([list3])
        # print(result[0])
        if result[0]==1.0:
            res = 'High productivity'
        else:
            res = 'Medium productivity'
        
        context = {'user_inputs': list3, 'result': res}
        return render(request, 'classification/output.html', context)
    except:
        pass
    return render(request, 'classification/classifyhome.html')


