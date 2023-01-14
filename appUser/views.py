from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.

def loginUser(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            context.update({"hata":"Kullanıcı adı veya şifre yanlış!! "})
    
    return render(request,'users/login.html', context)