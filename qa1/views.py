from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'GPTindex.html')


def sign_up(request):
    if (request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')
        my_users = User.objects.create_user(name, email, password)
        my_users.save()
        print(name, email, password)
        return render(request, 'login.html')

        # if password != c_password:
        #     print('Passwords do not match')
        # else:
        #     my_users.save()
        #     return render(request, 'login.html')
    return render(request, 'GPTsignup.html')


def login_costom(request):
    if (request.method == 'POST'):
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(email, username, password)
            return redirect(home)
        else:
            return HttpResponse('New User')
    return render(request, 'login.html')


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


def logout_custom(request):
    logout(request)
    return redirect('login')
