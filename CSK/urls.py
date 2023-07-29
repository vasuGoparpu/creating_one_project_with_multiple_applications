from django.urls import path

from CSK.views import *


app_name='chennai'


urlpatterns=[
    path('msd/',msd,name='msd'),
    path('jadeja/',jadeja,name='jadeja'),
    path('chennai/',chennai,name='chennai')
]