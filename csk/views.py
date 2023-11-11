from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def msd(request):
    return render(request,'msd.html')

def jaddu(request):
    return render(request,'jaddu.html')

def raina(request):
    return HttpResponse('''<center>
        <h1>Suresh raina is the best all rounder</h1>
        <h1 style="color:yellow;"><marquee behavior="alternate" direction="left">Best Lefthand Batsman</marquee></h1>
    </center>''')


