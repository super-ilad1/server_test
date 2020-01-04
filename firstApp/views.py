from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt



def home(request):
    return render(request,'index2.html')


@csrf_exempt
def submit(request):
    if request.method=='POST':


        updatedInfos = json.loads(request.body.decode('utf-8'))
        name=updatedInfos.get('name')
        age=updatedInfos.get('age')
        print(name,age)
        return JsonResponse({'name': 'OK'})

def sub_home(request):
    return render(request,'sub_home.html')
