from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

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
        if password !=c_password:
            alert=HttpResponse('password are not same')
            return render(request,'GPTsignup.html')        
        else:
            my_users.save()
            return render(request,'login.html')
        return render(request,'GPTsignup.html') 

def login(request):
    return render (request,'index.html')
