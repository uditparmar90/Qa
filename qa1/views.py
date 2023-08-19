from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request,'GPTindex.html')
    # return HttpResponse("vdfsdf")

def sign_up(request):
    return render(request,'GPTsignup.html')
