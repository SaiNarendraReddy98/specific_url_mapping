from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sachin(request):
    return render(request,'sachin.html')

def dhoni(request):
    return render(request,'dhoni.html')

def rohit(request):
    return HttpResponse('''<center>
        <h1>Rohit Sharma is the best Opener Batsman in India</h1>
        <h1 style="color:rgb(10, 169, 21);"><marquee behavior="alternate" direction="left">HIT-MAN</marquee></h1>
    </center>''')


