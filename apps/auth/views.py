from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def login(request):
    return render(request, 'auth/pages/login.html')


def register(request):
    return render(request, 'auth/pages/register.html')
