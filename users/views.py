from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from .forms import UserRegisterForm, UserLoginForm

# user register page
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account created for {}".format(username))
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})


# user login page
def login(request):
    form = UserLoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('user_name')
        password = form.cleaned_data.get('pass_word')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(request, "User authenticated. Welcome!")
            auth_login(request, user)
            return redirect('home')
        else:
            messages.warning(request, "Authentication failed. Please try again.")
            return render(request, 'users/login.html', {'form': form})
    return render(request, 'users/login.html', {'form': form})

# view allowing user to log out
def logout(request):
    auth_logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('home')
