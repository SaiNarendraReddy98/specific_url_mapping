from django.urls import path
from India.views import *

app_name = 'India'

urlpatterns = [
    path('sachin/',sachin,name='sachin'),
    path('dhoni/',dhoni,name='dhoni'),
    path('rohit/',rohit,name='rohit'),
    
]