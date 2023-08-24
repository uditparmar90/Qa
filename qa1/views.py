from django.http import HttpResponse
from django.shortcuts import render
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
        my_users.save()
        return render(request,'login.html')





        print(name,email,number,gender,password,c_password)

    return render(request,'GPTsignup.html')

def login(request):
    return render (request,'index.html')
