from django.shortcuts import render
from django.http import HttpResponse
import pickle
# Create your views here.

def regre(request):
    try:
        data = request.GET
        age1 = data['house_age']  # this is intentionally done only to generate error if data is empty 
        print(data)
        list3 = [int(data[i]) for i in data.keys()]
        pickle_in = open('real_estate.pickle', 'rb')
        reg = pickle.load(pickle_in)
        result = reg.predict([list3])
        # print(result[0])
        data1 = dict()
        for i in data.keys():
            data1[i] = int(data[i])
        print(data1)
        context = {'user_inputs': data1, 'result': result[0]}
        return render(request, 'regression/regoutput.html', context)
    except:
        pass
    return render(request, 'regression/regrehome.html')