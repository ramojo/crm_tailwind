from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
def index(request):
    # Check to see whether someone is logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate handled here
        user = authenticate(request, username=username, password1=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('index')
    else:
        return render(request, 'index.html')

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out!')
    return redirect('index')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            # Authenticate and login user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully registered!')
            return redirect('index')
    else:
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'register.html', context)
    return render(request, 'register.html')