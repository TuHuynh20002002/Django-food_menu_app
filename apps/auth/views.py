from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def authGetLogin(request):
    if request.user.is_authenticated:
        return redirect('foods:getIndex')
    return render(request, 'auth/pages/login.html')


def authGetRegister(request):
    if request.user.is_authenticated:
        return redirect('foods:getIndex')
    return render(request, 'auth/pages/register.html')


def authPostRegister(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password_confirmation = request.POST.get('password_confirmation')

    if User.objects.filter(username=username).exists():
        messages.error(request, 'Username already exists')
        return redirect('auth:getRegister')

    if User.objects.filter(email=request.POST.get('email')).exists():
        messages.error(request, 'Email already exists')
        return redirect('auth:getRegister')

    if password != password_confirmation:
        messages.error(request, 'Password confirmation does not match')
        return redirect('auth:getRegister')

    user = User.objects.create_user(username.lower(), email.lower(), password)
    user.save()
    return redirect('auth:getLogin')


def authPostLogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username.lower(), password=password)

    if user is None:
        messages.error(request, 'Invalid credentials')
        return redirect('auth:getLogin')

    print(user)
    login(request, user)
    return redirect('foods:getIndex')


def authPostLogout(request):
    logout(request)
    return redirect('base:getIndex')
