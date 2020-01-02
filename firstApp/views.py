from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.




def home(request):
    return render(request,'index.html')

def sub_home(request):
    return render(request,'sub_home.html')
