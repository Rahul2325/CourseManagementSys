from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
# from . models import Regform
from . models import Userlist
# from django.contrib.auth.models import User
# from django.contrib.auth import logout, authenticate, login

# from django.forms import modelform_factory

# reg_form = modelform_factory(Regform, exclude=[])

# Create your views here.
#example
def Catalog(request):
    # print(request.user)
    # if request.user.is_anonymous:
    #     return redirect('secsignin')
    # data = Regform.objects.all()
    # fdata = data.filter(id=Update_Profile)
    return render(request,'cms/Catalog.html')

def CC(request):
    context = {}
    return render(request,'cms/CC.html',context)

def CO(request):
    context = {}
    return render(request,'cms/CO.html',context)

# def Update_Profile(request):
    
#     Register=Regform.objects.all()
#     print(Register)
#     return render(request,'cms/Update_Profile.html',{'Register': Register})

def Preview(request):
    context={}
    return render(request, 'cms/Preview.html', context)



def register(request):
    if request.method=="POST":
        # register = reg_form(request.POST)
        # # fname=register.cleaned_data.get('firstName')
        # email=request.POST.get('email')
        # password=request.POST.get('password')
        fname =request.POST['firstName']
        lname =request.POST['lastName']
        DOB =request.POST['DOB']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        username=request.POST['username']
        if password==password2:
            if Userlist.objects.filter(email=email).exists():
                return HttpResponse("Email already exists")
            else:
                register=Userlist(firstName=fname,lastName=lname,username=username,email=email,password=password,password2=password2, DOB=DOB)
                register.save()
                # Userlist(user_id=register.id, DOB=DOB).save()
                # Userlist(user_id=register, password2=password2).save()
                # print(register.id)
                # context={
                #     "firstname":fname,
                #     "lastname":lname
                # }
                return render(request, 'cms/display.html')
        else:
            return HttpResponse("Password Dosen't Match")
    else:
        return render(request, 'cms/register.html')


    #     if register.is_valid():
    #         register.save()
    #         user = User.objects.create_user(email,password)
    #         user.save()
    #         return render(request, 'cms/display.html')
    #     else:
    #         return render(request, 'cms/register.html')
    # else:    
    #     return render(request, 'cms/register.html')    

def display(request):
    context={}
    return render(request, 'cms/display.html', context)

# Login authentication


def secsignin(request):
    # print(request)
    # user_id=request.user.id
    # print(user_id)
    if request.method=="POST":
        # print(request.POST['emailid'])
        # print(request.POST['password'])
        email = request.POST['email']
        password= request.POST['password']
        if Userlist.objects.filter(email=email).exists():
            if Userlist.objects.filter(password=password).exists():
                context={
                        "email":email,

                }
                return render(request, 'cms/Catalog.html', context)
            else:
                return HttpResponse("Wrong Password")
        else:
            return HttpResponse("Invalid Email")
    else:
        return render(request, 'cms/secsignin.html')



def Update_Profile(request, user_id):
    data = Userlist.objects.all() #importing all the dataa from the db
    fdata = data.filter(id=user_id)
    # print(fdata,"888888888")
    # print(data)
    print(fdata,"==============")

    return render(request,'cms/Update_Profile.html',{'Register': fdata})
    

        
        # if user has entered the correct credentials
        # user = authenticate(email=emailid, password=password)
        
        # if user is not None:
        #     login(request, user)
            # A backend authenticated the credentials
            # return redirect("Catalog")
        # else:
        #     return render(request, 'cms/secsignin.html', )
            # No backend authenticated the credentials
    # return render(request, 'cms/secsignin.html')

# def secsignout(request):
#     logout(request)
#     return redirect('cms/secsignin')

