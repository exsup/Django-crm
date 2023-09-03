from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

# Create your views here.

def home(request):
        # now lets check to see logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authentification
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Logged In Sucessfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('home')
    else:
        return render(request, 'home.html',{})
            
    


def login_user(request):
    pass


def logout_user(request):

    logout(request)
    messages.success(request, 'You have been Logged Out....')
    return redirect('home')


def register(request):
    return render(request, 'register.html',{})
