from django.shortcuts import render
from django.http import HttpResponse
from .forms import cakeform

# Create your views here.
def home(request):
    return render(request,"index.html")
def order(request):
    forms1= cakeform()
    return render(request,"order.html",{"form":forms1})