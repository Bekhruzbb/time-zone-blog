from django.contrib import admin
from .models import Cart, CartItem, OrderItem, Checkout
# Register your models here.
admin.site.register([Cart, CartItem, OrderItem, Checkout])
