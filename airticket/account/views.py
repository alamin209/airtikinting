from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def login(request):
     if request.method =="POST":
           username=request.POST['username']
           password=request.POST['password']
           user=auth.authenticate(username=username,password=password)
           if user is not None:
               auth.login(request,user)
               return redirect('/')
           else:
                 messages.info(request ,"Invalid username and password")
                 return redirect('login')   
     else:   
      return render(request,'login.html')


def register(request):
    if request.method =="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password1']
        password1=request.POST['password2']
        
        if  password == password1:
            if User.objects.filter(username = username).exists():
                messages.info(request ,"User name Alreadty taken")
                return redirect('register')
                # print("User name already taken")
            elif User.objects.filter(email = email).exists():
                messages.info(request ,"Email Already Taken")
                return redirect('register')
            else:         
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print("User Created Successfully")
                return redirect('login')
        else:
            messages.info(request ,"Password do not Match")
            return redirect('register')            
    else:   
      return render(request,'register.html')
  
def logout(request):
    auth.logout(request)
    return redirect('/')
