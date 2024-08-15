from django.contrib import admin
from .models import Item, Cart_session, Cart_item, Order, Order_item

# Register your models here.
admin.site.register([Item, Cart_session, Cart_item, Order, Order_item])