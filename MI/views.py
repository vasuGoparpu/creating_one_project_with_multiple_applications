from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def rohith(request):
    return render(request,'rohith.html')


def surya(request):
    return render(request,'surya.html')



def boomra(request):
    return HttpResponse('Boomra is one of the best bowler in MI')