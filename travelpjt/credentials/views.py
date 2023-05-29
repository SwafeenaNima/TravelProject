from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        pwd = request.POST['pwd']
        user=auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Entry.')
            return redirect('login')
    return render(request, 'login.html')

def register(request):

    if request.method=='POST':
        uname=request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pwd = request.POST['pwd']
        cpwd = request.POST['cpwd']
        if pwd == cpwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username already exists. Try another one")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email is already exists. Try another one")
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,first_name=fname, last_name=lname, email=email,password=pwd)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request, "Passwords not matching")
            return redirect('register')
        return redirect('/')
    return  render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
