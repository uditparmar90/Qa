from imaplib import _Authenticator
from multiprocessing import AuthenticationError
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    
    return render(request,'GPTindex.html')
    # return HttpResponse("vdfsdf")

def sign_up(request):
    if(request.method=='POST'):
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        c_password=request.POST.get('c_password')
        my_users=User.objects.create_user(name,email,password)
        my_users.save()
        return render(request,'login.html')
        # if password !=c_password:
        #     #  messages.error(request, 'Passwords do not match') 
        #     err=('Passwords do not match')     
        # else:
        #     my_users.save()
        #     return render(request,'login.html')
    return render(request,'GPTsignup.html') 


def login_costom(request):
    if(request.method=='POST'):
        username= request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            return HttpResponse('New User')
    
    return render (request,'login.html')
def home(request):
    return render(request,'home.html')
