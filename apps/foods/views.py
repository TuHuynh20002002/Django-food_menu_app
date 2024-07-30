from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import re


@login_required
def foodsGetIndex(request):
    return render(request, 'foods/pages/index.html')


@login_required
def foodsGetOrders(request):
    return render(request, 'foods/pages/orders.html')


@login_required
def foodsGetLocations(request):
    return render(request, 'foods/pages/locations.html')


@login_required
def foodsGetRewards(request):
    return render(request, 'foods/pages/rewards.html')
