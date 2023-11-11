from rcb.views import *
from django.urls import path

app_name ='RCB'

urlpatterns = [
    path('virat/',virat,name='virat'),
    path('siraj/',siraj,name='siraj'),
    path('maxwell/',maxwell,name='maxwell'),
    
]