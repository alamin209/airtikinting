from django.shortcuts import render
from   .models import Destination
from django.http import HttpResponse

def index(request):
   
    dests=Destination.objects.all()
    # dest1
    return render (request,"index.html",{ 'dests':dests })
    
