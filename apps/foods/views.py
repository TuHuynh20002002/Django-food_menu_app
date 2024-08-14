import re
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import json
from .models import Item, Cart_session, Cart_item


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
    cart_session, created = Cart_session.objects.get_or_create(user=request.user)
    cart_items = Cart_item.objects.filter(cart_session=cart_session)
    return render(request, 'foods/pages/orders.html', {'cart_items': cart_items, 'cart_session': cart_session})


@login_required
def foodsGetLocations(request):
    return render(request, 'foods/pages/locations.html')


@login_required
def foodsGetRewards(request):
    return render(request, 'foods/pages/rewards.html')


@login_required
def cartItemGetQuantity(request):
    cart_session, created = Cart_session.objects.get_or_create(user=request.user)
    cart_items = Cart_item.objects.filter(cart_session=cart_session)
    return JsonResponse({'quantity': len(cart_items)})


@login_required
def cartItemAdd(request):
    data = json.loads(request.body)
    item_id = data['item_id']
    item_quantity = int(data['item_quantity'])  
    item = Item.objects.get(pk=item_id)
    
    cart_session, created = Cart_session.objects.get_or_create(user=request.user)
    cart_item, created = Cart_item.objects.get_or_create(cart_session=cart_session, item=item)
    
    cart_item.quantity += item_quantity
    cart_item.save()
    
    cart_session.total += cart_item.total()
    cart_session.save()
    
    cart_items = Cart_item.objects.filter(cart_session=cart_session)
    return JsonResponse({'quantity': len(cart_items)})


@login_required
def cartItemRemove(request):
    item_id = request.POST.get('item_id')
    item = Item.objects.get(pk=item_id)
    
    cart_session, created = Cart_session.objects.get_or_create(user=request.user)
    cart_item = Cart_item.objects.get(cart_session=cart_session, item=item)
    
    cart_session.total -= cart_item.total()
    cart_session.save()
    
    cart_item.delete()
    
    cart_items = Cart_item.objects.filter(cart_session=cart_session)
    return redirect('foods:getOrders')