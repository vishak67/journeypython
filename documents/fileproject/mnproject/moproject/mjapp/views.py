from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from . models import place,food

def fill(request):
    obj=place.objects.all()
    ob=food.objects.all()
    return render(request,"index.html",{'result':obj},{'result':ob})


