from django.urls import path
from MI.views import *
app_name='mumbai'

urlpatterns=[
    path('rohith/',rohith,name='rohith'),
    path('surya/',surya,name='surya'),
    path('boomra/',boomra,name='boomra')
]