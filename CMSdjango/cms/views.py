from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from .forms import SignUpForm, EditUserProfileForm, CourseForm
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate, login, logout

# from . models import Regform
# from . models import User
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
    if request.user.is_authenticated:
        courses=Course.objects.all()
        return render(request,'cms/Catalog.html', {'courses':courses})
    else:
        return HttpResponseRedirect('/')

def CC(request):
    if request.user.is_authenticated:
        print(request.method)
        if request.method=="POST":
            form=CourseForm(request.POST, request.FILES)
            print(form, "aaaaaaaaaaaaa")
            if form.is_valid():
                # form= form.save()
                cname=request.POST.get('CourseName')
                desc=request.POST.get('Desc')
                cimage=request.FILES['CourseImage']
                credit=request.POST.get('CourseCredits')
                Tags=request.POST.get('Tags')
                print("hello")
                pst=Course(CourseName=cname, Desc=desc, CourseImage=cimage, CourseCredits=credit, Tags=Tags)
                pst.save()
                # print(pst,"bbbbbbbbbbb")
                form=CourseForm()

        else:
            form=CourseForm()

        return render(request,'cms/CC.html', {'form':form})
    else:
        return HttpResponseRedirect('/')

def CO(request):
    if request.user.is_authenticated:
        return render(request,'cms/CO.html', {'name':request.user})
    else:
        return HttpResponseRedirect('/')

# def Update_Profile(request):
    
#     Register=Regform.objects.all()
#     print(Register)
#     return render(request,'cms/Update_Profile.html',{'Register': Register})

def Preview(request):
    context={}
    return render(request, 'cms/Preview.html', context)



# def register(request):
#     if request.method=="POST":
#         # register = reg_form(request.POST)
#         # # fname=register.cleaned_data.get('firstName')
#         # email=request.POST.get('email')
#         # password=request.POST.get('password')
#         fname =request.POST['firstName']
#         lname =request.POST['lastName']
#         DOB =request.POST['DOB']
#         email=request.POST['email']
#         password=request.POST['password']
#         password2=request.POST['password2']
#         username=request.POST['username']
#         if password==password2:
#             if Userlist.objects.filter(email=email).exists():
#                 return HttpResponse("Email already exists")
#             else:
#                 register=Userlist(firstName=fname,lastName=lname,username=username,email=email,password=password,password2=password2, DOB=DOB)
#                 register.save()
#                 # Userlist(user_id=register.id, DOB=DOB).save()
#                 # Userlist(user_id=register, password2=password2).save()
#                 # print(register.id)
#                 # context={
#                 #     "firstname":fname,
#                 #     "lastname":lname
#                 # }
#                 return render(request, 'cms/display.html')
#         else:
#             return HttpResponse("Password Dosen't Match")
#     else:
#         return render(request, 'cms/register.html')


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


# def secsignin(request):
    # print(request)
    # user_id=request.user.id
    # print(user_id)
    # if request.method=="POST":
    #     # print(request.POST['emailid'])
    #     # print(request.POST['password'])
    #     email = request.POST['email']
    #     password= request.POST['password']
    #     if User.objects.filter(email=email).exists():
    #         if Userlist.objects.filter(password=password).exists():
    #             context={
    #                     "email":email,

    #             }
    #             return render(request, 'cms/Catalog.html', context)
    #         else:
    #             return HttpResponse("Wrong Password")
    #     else:
    #         return HttpResponse("Invalid Email")
    # else:
    #     return render(request, 'cms/secsignin.html')



# def Update_Profile(request, user_id):
#     print(user_id)
#     data = User.objects.all() #importing all the dataa from the db
#     fdata = data.filter(id=user_id)
#     # print(fdata,"888888888")
#     # print(data)
#     print(fdata,"==============")

#     return render(request,'cms/Update_Profile.html',{'Register': fdata})
    

        
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

#Sign up View function
def sign_up(request):
    # print(request.method)
    if request.method == "POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account Created Successfully!!!')
            print(form)
            form.save()
    else:
        print("else")
        form= SignUpForm()
    return render(request, 'cms/register.html', {'form':form})

#Login View
def user_login(request):
    # print(request) 
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            print(form.is_valid())
            if form.is_valid():
                print("validddddddd")
                uname = request.POST.get('username')
                upass = request.POST.get('password')
                user = authenticate(username = uname, password = upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in successfully!!")
                    return redirect('/Catalog')
        else:
            print("Heloooooooooo")
            form = AuthenticationForm()
        return render(request, 'cms/secsignin.html', {'form': form})
    else:
        return HttpResponseRedirect('/Catalog')

# Profile Page
def user_profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form = EditUserProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, "Profile Updated!!!")
                form.save()
        else:
            form=EditUserProfileForm(instance=request.user)
        return render(request, 'cms/Update_Profile.html', {'name':request.user, 'form':form})
    else:
        return HttpResponseRedirect('/')

#Logout
def user_logout(request):
    logout(request)
    print("logout")
    return HttpResponseRedirect('/')

#Change Password
def user_change_pass(request):
    if request.method=="POST":
        fm=PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/profile')
    else:
        fm=PasswordChangeForm(user=request.user)
    return render(request, 'cms/changepass.html', {'name':request.user,'form':fm})

