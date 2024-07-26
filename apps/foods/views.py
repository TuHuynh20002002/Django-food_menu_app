from django.shortcuts import render
from django.http import JsonResponse
import re


def index(request):
    return render(request, 'foods/pages/index.html')


def orders(request):
    return render(request, 'foods/pages/orders.html')


def locations(request):
    return render(request, 'foods/pages/locations.html')


def rewards(request):
    return render(request, 'foods/pages/rewards.html')
