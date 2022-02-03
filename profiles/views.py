from django.shortcuts import render, redirect
from .forms import UserSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.

def signup(request):
    if request.POST:
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = UserSignUpForm()
    
    return render(request, "profiles/signup.html", {"form": form})

def signin(request):
    if request.POST:
        form = AuthenticationForm(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            if "@" in username:
                user_object = User.objects.get(email=username)
                username = user_object.username
        except:
            pass

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("success")
    else:
        form = AuthenticationForm()

    return render(request, "profiles/signin.html", {"form": form})