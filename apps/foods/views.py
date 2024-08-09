import re
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Item


@login_required
def foodsGetIndex(request):
    items_list = Item.objects.all()
    return render(request, 'foods/pages/index.html', {'items': items_list})


@login_required
def foodsGetDetails(request, item_id):
    item = Item.objects.get(pk=item_id)
    return render(request, 'foods/pages/details.html', {'item': item})


@login_required
def foodsGetOrders(request):
    return render(request, 'foods/pages/orders.html')


@login_required
def foodsGetLocations(request):
    return render(request, 'foods/pages/locations.html')


@login_required
def foodsGetRewards(request):
    return render(request, 'foods/pages/rewards.html')
