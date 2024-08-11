from django.db import models
from django.contrib.auth.models import User

# Static Models
class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='')
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Discount(models.Model):
    code = models.CharField(max_length=10)
    discount = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code


# Session Models
class Cart_session(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Cart_item(models.Model):
    cart_session = models.ForeignKey('Cart_session', on_delete=models.CASCADE)
    item_id = models.ForeignKey('Item', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_id.title

    def total(self):
        return self.item_id.price * self.quantity


# Processed Models
class Payment(models.Model):
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    method = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    payment_id = models.ForeignKey('Payment', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order_item(models.Model):
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE)
    item_id = models.ForeignKey('Item', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
