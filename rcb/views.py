from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return render(request,'virat.html')

def siraj(request):
    return render(request,'siraj.html')

def maxwell(request):
    return HttpResponse('''<center>
        <h1> Gleen MaxWell is the best batsman</h1>
        <h1 style="color:green;"><marquee behavior="alternate" direction="left">Best Batsman</marquee></h1>
    </center>''')


