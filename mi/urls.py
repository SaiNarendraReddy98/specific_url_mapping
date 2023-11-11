from mi.views import *
from django.urls import path

app_name = 'MI'

urlpatterns = [

    path('sachin/',sachin,name='sachin'),
    path('rohit/',rohit,name='rohit'),
    path('bhumra/',bhumra,name='bhumra'),
    
]