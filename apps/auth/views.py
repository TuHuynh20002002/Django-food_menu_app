from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


def authGetLogin(request):
    return render(request, 'auth/pages/login.html')


def authGetRegister(request):
    return render(request, 'auth/pages/register.html')


def authPostRegister(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password_confirmation = request.POST.get('password_confirmation')

    if User.objects.filter(username=username).exists():
        messages.error(request, 'Username already exists')
        return redirect('/auth/register')

    if User.objects.filter(email=request.POST.get('email')).exists():
        messages.error(request, 'Email already exists')
        return redirect('/auth/register')

    if password != password_confirmation:
        messages.error(request, 'Password confirmation does not match')
        return redirect('/auth/register')

    user = User.objects.create_user(username.lower(), email.lower(), password)
    user.save()
    return redirect('/auth/login')


def authPostLogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username.lower(), password=password)

    if user is None:
        messages.error(request, 'Invalid credentials')
        return redirect('/auth/login')

    print(user)
    login(request, user)
    return redirect('/foods/')


def authPostLogout(request):
    logout(request)
    return redirect('/')
