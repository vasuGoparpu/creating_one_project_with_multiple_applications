from django.shortcuts import render
from django.http import *
# Create your views here.

def msd(request):
    return render(request,'msd.html')


def jadeja(request):
    return render(request,'jadeja.html')

def chennai(request):
    return HttpResponse('chennai is won the match')