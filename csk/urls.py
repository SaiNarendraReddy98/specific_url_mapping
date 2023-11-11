from csk.views import *
from django.urls import path


app_name='CSK'

urlpatterns = [
    path('msd/',msd,name='msd'),
    path('jaddu/',jaddu,name='jaddu'),
    path('raina/',raina,name='raina'),
]