from asyncio import Task
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import task

from qa1.models import task


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
    if request.method == 'POST':
        title = request.POST.get('newTask')
        date = request.POST.get('reminderDate')
        time = request.POST.get('reminderTime')
        try:
            new_task = task(title=title, date=date, time=time)  # Use Task, not task
            new_task.save()
            tasks = task.objects.all().order_by('title')  # Retrieve all tasks from the database
            context = {'task': tasks}
            return render(request, 'home.html', context)
        except Exception as e:
            print(f"Error: {str(e)}")   

    tasks = task.objects.all().order_by('-title')  # Retrieve all tasks from the database
    context = {'task': tasks}
    return render(request, 'home.html', context)

def logout_custom(request):
    logout(request)
    return redirect('login')

# def addtask(request):

#     if(request.method=='POST'):
#         title=request.POST.get('newTask')
#         date=request.POST.get('reminderDate')
#         time=request.POST.get('reminderTime')
#         print(title,date,time)
#         data={
#                 'title':title,'date':date,'time':time
#             }
#         try:
#             new_task = task(title=title, date=date, time=time)
#             new_task.save()
            
#             # return redirect(new_task)

#         except Exception as e:
#             print(f"Error: {str(e)}")

#         return redirect(request,'home.html',data)

#     return HttpResponse (request)

