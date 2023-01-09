from django.shortcuts import render

# Create your views here.


def index(request):
    
    return render(request,'index.html')

def About(request):
    
    return render(request,'about.html')

def Services(request):
    
    return render(request,'services.html')

def Contact(request):
    
    return render(request,'contact.html')

