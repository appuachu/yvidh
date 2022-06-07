from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
# Create your views here.

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:

            messages.error(request,'Invalid credential')
            return redirect('login')

    else:
        return render(request,"login.html")


def register(request):
    if request.method=="POST":
        fullname=request.POST['fullname']
        number = request.POST['number']
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']



        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.error( request,"Username is already exists ")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'email already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=fullname,last_name=number, username=username, email=email, password=password)
                user.save();
                return redirect('login')

        else:
            print('not created')
            return redirect('register')

    else:
        return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')