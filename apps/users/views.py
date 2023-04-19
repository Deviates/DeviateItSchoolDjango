from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.db import IntegrityError
from django.contrib import messages
from .models import User
from apps.settings.models import Setting

# Create your views here.
def register(request):
    setting = Setting.objects.latest("id")
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        try:
        
            if password == confirm_password:
                user = User.objects.create(username=username,email=email)
                user.set_password(password)
                user.save()
                user = User.objects.get(username=username)
                user = authenticate(username = username, password = password)
                user.save()
                login(request, user)
                return redirect('index')
        except IntegrityError:
            messages.error(request, 'Неправильный пароль.')
            return redirect('register')
    context = {
        "setting": setting,
    }
    return render(request, "users/signup.html", context)

def us_login(request):
    setting = Setting.objects.latest("id")
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Пользователь с таким именем не существует.')
            return redirect('login')
        user = authenticate(username = username,password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Неправильный пароль.')
            return redirect('login')
    context = {
        "setting": setting,
    }
    return render(request, "users/signin.html", context)

def profile(request):
    setting = Setting.objects.latest("id")
    user = request.user
    context = {
        "setting": setting,
        "user": user
            }
    return render(request, "users/settings.html", context)