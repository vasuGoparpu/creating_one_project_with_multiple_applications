from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def virat(request):
    return render(request,'virat.html')

def rcb(request):
    return render(request,'rcb.html')

def cup(request):
    return HttpResponse('RCB NOT WON  THE TROPHY BUT WON THE HEARTS')