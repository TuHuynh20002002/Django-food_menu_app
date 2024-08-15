import re
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import json
from .models import Item, Cart_session, Cart_item, Order, Order_item


@login_required
def foodsGetIndex(request):
    items_list = Item.objects.all()
    return render(request, 'foods/pages/index.html', {'items': items_list})


@login_required
def foodsGetDetails(request, item_id):
    item = Item.objects.get(pk=item_id)
    return render(request, 'foods/pages/details.html', {'item': item})


@login_required
def foodsGetCart(request):
    cart_session, created = Cart_session.objects.get_or_create(user=request.user)
    cart_items = Cart_item.objects.filter(cart_session=cart_session)
    return render(request, 'foods/pages/cart.html', {'cart_items': cart_items, 'cart_session': cart_session})


@login_required
def foodsGetOrders(request):
    orders = Order.objects.filter(user=request.user)
    order_items = Order_item.objects.filter(order__in=orders)
    return render(request, 'foods/pages/orders.html', {'order_items': order_items, 'orders': orders.order_by('-created_at')})


@login_required
def foodsGetCartItemQuantity(request):
    cart_session, created = Cart_session.objects.get_or_create(user=request.user)
    cart_items = Cart_item.objects.filter(cart_session=cart_session)
    return JsonResponse({'quantity': len(cart_items)})


@login_required
def foodsPostCartItemAdd(request):
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
def foodsPostCartItemRemove(request):
    item_id = request.POST.get('item_id')
    item = Item.objects.get(pk=item_id)

    cart_session, created = Cart_session.objects.get_or_create(user=request.user)
    cart_item = Cart_item.objects.get(cart_session=cart_session, item=item)

    cart_session.total -= cart_item.total()
    cart_session.save()

    cart_item.delete()

    cart_items = Cart_item.objects.filter(cart_session=cart_session)
    return redirect('foods:getCart')


@login_required
def foodsPostCartItemPurchase(request):
    cart_session, created = Cart_session.objects.get_or_create(user=request.user)
    cart_items = Cart_item.objects.filter(cart_session=cart_session)
    print(cart_items)
    print(cart_session.total)
    
    # Create a new Order instance
    order = Order.objects.create(user=request.user, total=cart_session.total)

    # Create OrderItem instances for each Cart_item
    for cart_item in cart_items:
        Order_item.objects.create(
            order=order,
            item=cart_item.item,
            quantity=cart_item.quantity,
        )
    
    cart_items.delete()
    cart_session.total = 0
    cart_session.save()
    return redirect('foods:getCart')