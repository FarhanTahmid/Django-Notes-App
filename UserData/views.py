from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import UserInfo
# Create your views here.

def landingPage(request):
    return render(request,'index.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
    
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('UserData:notes_home',username)
        else:
            print("Credentials dont match")
            
    return render(request,'login.html')

def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if(password==confirm_password):
            if(User.objects.filter(username=username).exists()):
                messages.error(request,"User already exists")            
            else:
                new_user=User.objects.create_user(username=username,email=email,password=password)
                new_user.save()
                
                new_user_for_table=UserInfo.objects.create(email=email,username=username)
                new_user_for_table.save()
                print("User stored in database")
                messages.success(request,"Account Created Successfully")
                return redirect('UserData:login')
        else:
            messages.error(request,"Two Passwords do not match")
    return render(request,'signup.html')

def notes_home(request,username):
    context={
        'username2':username
    }
    return render(request,'notes_home.html',context=context)