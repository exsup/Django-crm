from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm  # Assuming the forms module is in the same directory as your views
from .models import Record

# Create your views here.

def home(request):
    records = Record.objects.all()
    # Check for POST request for login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authentication
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged In Successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})


def login_user(request):
    pass  # Add your login functionality here


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been Logged Out....')
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Account Created Successfully!')
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        #check for records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, 'You Must Be Logged In!')
        return redirect('home')