from django.urls import path

from RCB.views import *

app_name='bangalore'

urlpatterns=[
    path('virat/',virat,name='virat'),
    path('rcb/',rcb,name='rcb'),
    path('cup/',cup,name='cup'),
]