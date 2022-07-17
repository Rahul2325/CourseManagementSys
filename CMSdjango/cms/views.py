from django.shortcuts import render
from .models import *
from datetime import datetime

from django.forms import modelform_factory

reg_form = modelform_factory(Regform, exclude=[])

# Create your views here.
#example
def Catalog(request):
    context = {}
    return render(request,'cms/Catalog.html',context)

def CC(request):
    context = {}
    return render(request,'cms/CC.html',context)

def CO(request):
    context = {}
    return render(request,'cms/CO.html',context)

def Update_Profile(request):
    context = {}
    return render(request,'cms/Update_Profile.html',context)

def Preview(request):
    context={}
    return render(request, 'cms/Preview.html', context)

def secsignin(request):
    context={}
    return render(request, 'cms/secsignin.html', context)

def register(request):
    if request.method=="POST":
        register = reg_form(request.POST)
        # fname =request.POST['firstName']
        # Lname =request.POST['lastName']
        # DOB =request.POST['DOB']
        # email=request.POST['email']
        # password=request.POST['password']
        # username=request.POST['username']
        # register=Regform(firstName=fname,lastName=Lname,username=username,email=email,password=password,DOB=DOB)
        if register.is_valid():
            register.save()
            return render(request, 'cms/display.html')
        else:
            return render(request, 'cms/register.html')
    else:    
        return render(request, 'cms/register.html')    

def display(request):
    context={}
    return render(request, 'cms/display.html', context)
