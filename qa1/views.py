from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def default(request):
    return render(request,'login.html')
    # return HttpResponse("vdfsdf")

def temp(request):
    return render(request,'Ashesh.html')
