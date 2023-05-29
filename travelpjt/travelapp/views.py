from django.shortcuts import render
from django.http import HttpResponse
from . models import Place
from . models import Ourteam

# Create your views here.

def demo(request):
    places=Place.objects.all()
    team=Ourteam.objects.all()
    #return HttpResponse("Hello World")
    return render(request,'index.html',{'places':places,'team':team})

def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')