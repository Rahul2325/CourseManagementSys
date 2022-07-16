from django.shortcuts import render

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
