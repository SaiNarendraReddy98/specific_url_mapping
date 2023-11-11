from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sachin(request):
    return HttpResponse('''<center>
        <h1 style="color:grey">Sachin Tendulkar is the Master of the cricket</h1>
        <h1 style="color:blue;"><marquee behavior="alternate" direction="left">Best Batsman</marquee></h1>
    </center>''')

def rohit(request):
    return render(request,'rohit.html')

def bhumra(request):
    return render(request,'bhumra.html')

