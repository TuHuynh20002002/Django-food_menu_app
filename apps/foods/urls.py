"""
URL configuration for THfood project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path

app_name = 'foods'

urlpatterns = [
    path('', views.foodsGetIndex, name='getIndex'),
    path('details/<int:item_id>/', views.foodsGetDetails, name='getDetails'),
    path('cart/', views.foodsGetCart, name='getCart'),
    path('orders/', views.foodsGetOrders, name='getOrders'),

    path('cart-item-quantity/', views.foodsGetCartItemQuantity, name='getCartItemQuantity'),
    path('cart-item-add/', views.foodsPostCartItemAdd, name='postCartItemAdd'),
    path('cart-item-remove/', views.foodsPostCartItemRemove, name='postCartItemRemove'),
    path('cart-item-purchase/', views.foodsPostCartItemPurchase, name='postCartItemPurchase'),
]
